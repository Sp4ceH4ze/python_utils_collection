# python_utils_collection

A growing collection of reusable Python utility scripts. Each script works as both a CLI tool and an importable module.

---

## Setup

**Requirements:** Python 3.14+

```bash
git clone https://github.com/sp4c3h4z3/python_utils_collection
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
└── utils/
    ├── __init__.py
    └── file/
        ├── __init__.py
        └── checksum.py
```

---

## Utilities

### `checksum` — File & String Hashing

Hash files, directories, and strings. Optionally verify against a known checksum.

**Supported algorithms:** `md5`, `sha1`, `sha256`, `sha512`

**Usage**

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
from utils.file.checksum import hash_file, hash_directory, hash_string, hash_compare

# hash
result = hash_file("file.txt", "sha256")
result = hash_directory("/path/to/dir", "sha256")
result = hash_string("hello world", "sha256")

# verify
match, actual = hash_compare(result, expected)
if not match:
    raise ValueError(f"Checksum mismatch: {actual}")
```

---

## Conventions

- Every script works as both a CLI tool and an importable module
- CLI commands are registered via `pyproject.toml` and available after `pip install -e .`
- Scripts follow consistent CLI patterns: `--check`, `--dry-run`, `--verbose`, `--format`
- The venv should always be active when running CLI commands
