import os

import click

from utils.common import header, path, success, warning
from utils.security.checksum import hash_file


def find_duplicate(directory: str):
    hash_to_files = {}
    for root, dirs, files in os.walk(directory):
        dirs.sort()
        for file in sorted(files):
            filepath = os.path.join(root, file)
            file_hash = hash_file(filepath, "md5")
            if hash_to_files.get(file_hash):
                hash_to_files[file_hash].append(filepath)
            else:
                hash_to_files[file_hash] = [filepath]
    return {h: paths for h, paths in hash_to_files.items() if len(paths) > 1}


@click.command()
@click.argument("directory", type=click.Path(exists=True))
def main(directory: str):
    result = find_duplicate(directory)
    if not result:
        click.echo(success("No duplicates found."))
        return
    click.echo(warning(f"Found {len(result)} duplicate group(s):\n"))
    for file_hash, paths in result.items():
        click.echo(header(file_hash))
        for p in paths:
            click.echo(path(f" {p}"))
        click.echo("")


if __name__ == "__main__":
    main()
