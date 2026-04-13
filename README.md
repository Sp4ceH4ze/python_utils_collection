# python_utils_collection

A growing collection of reusable Python utility scripts. Each script works as both a CLI tool and an importable module.

---

## Setup

**Requirements:** Python 3.14+

```bash
git clone https://github.com/Sp4ceH4ze/python_utils_collection
cd python_utils_collection
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Project Structure

```
python_utils_collection/
├── .venv/
├── pyproject.toml
├── README.md
├── LICENSE.md
├── LICENSES/
│   └── gitleaks-MIT.md
└── utils/
    ├── __init__.py
    ├── common.py
    ├── file/
    │   ├── __init__.py
    │   ├── find_duplicates.py
    │   └── batch_rename.py
    └── security/
        ├── __init__.py
        ├── checksum.py
        ├── secret_scan.py
        └── rules/
            └── gitleaks.toml
```

---

## Utilities

### `checksum` — File & String Hashing

Hash files, directories, and strings. Optionally verify against a known checksum.

**Supported algorithms:** `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `sha3_224`, `sha3_256`, `sha3_384`, `sha3_512`, `shake_128`, `shake_256`, `blake2b`, `blake2s`, `md5`

**CLI**

```bash
# hash a file
checksum file path/to/file.txt sha256

# hash a directory
checksum file path/to/dir sha256

# hash a string
checksum string "hello world" sha256

# verify against a known checksum
checksum file path/to/file.txt sha256 --check a3f1c2...
checksum string "hello world" sha256 --check 2aae6c...
```

**Import**

```python
from utils.security.checksum import hash_file, hash_directory, hash_string, hash_compare

result = hash_file("file.txt", "sha256")
result = hash_directory("/path/to/dir", "sha256")
result = hash_string("hello world", "sha256")

match, actual = hash_compare(result, expected)
if not match:
    raise ValueError(f"Checksum mismatch: {actual}")
```

---

### `find_duplicates` — Duplicate File Detection

Walk a directory and find duplicate files by MD5 hash. Groups results by hash and reports all matching paths.

**CLI**

```bash
find_duplicates path/to/dir
```

**Import**

```python
from utils.file.find_duplicates import find_duplicate

duplicates = find_duplicate("/path/to/dir")
for hash, paths in duplicates.items():
    print(hash, paths)
```

---

### `batch_rename` — Bulk File Renaming

Rename files in bulk using string matching. Supports dry-run mode to preview changes before applying them.

**CLI**

```bash
# rename all .jpeg files to .jpg
batch_rename path/to/dir .jpeg .jpg

# preview changes without applying them
batch_rename path/to/dir .jpeg .jpg --dry-run
```

**Import**

```python
from utils.file.batch_rename import batch_rename, apply_renames

matches = batch_rename("/path/to/dir", ".jpeg", ".jpg")
apply_renames(matches, dry_run=True)   # preview
apply_renames(matches, dry_run=False)  # apply
```

---

### `secret_scan` — Secret & Credential Scanner

Scan files and directories for accidentally committed secrets, API keys, and credentials. Uses patterns from [gitleaks](https://github.com/gitleaks/gitleaks).

**CLI**

```bash
# scan a file
secret_scan path/to/file.py

# scan a directory
secret_scan path/to/dir
```

**Import**

```python
from utils.security.secret_scan import scan

matches = scan("/path/to/dir")
for item in matches:
    print(item['file'], item['line'], item['rule'], item['match'])
```

---

## Common Helpers

`utils/common.py` provides shared CLI output helpers used across all scripts:

```python
from utils.common import success, error, warning, path, header

click.echo(success("Operation completed."))
click.echo(error("Something went wrong."))
click.echo(warning("Proceed with caution."))
click.echo(path("/some/file/path"))
click.echo(header("Section title"))
```

---

## Conventions

- Every script works as both a CLI tool and an importable module
- CLI commands are registered via `pyproject.toml` and available after `pip install -e .`
- Scripts follow consistent CLI patterns: `--dry-run`, `--verbose`, `--format`
- Color output: green = success, red = error, yellow = warning, cyan = paths, white = headers
- The venv must be active when running CLI commands

## Attribution

Secret scanning patterns sourced from [gitleaks](https://github.com/gitleaks/gitleaks), licensed under MIT — see `LICENSES/gitleaks-MIT.md`.
