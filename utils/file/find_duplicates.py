import os

from utils.common import success, warning, path, header
from utils.security.checksum import hash_file, hash_compare

def find_duplicate(directory: str):
    hash_list = {}
    for root, dirs, files in os.walk(directory):
        dirs.sort()
        for file in sorted (files):
            filepath = os.path.join(root, file)
            hash = hash_file(filepath, "md5")
            if hash_list.get(hash):
                hash_list[hash].append(filepath)
            else:
                hash_list[hash] = [filepath]
    return {hash: paths for hash, paths in hash_list.items() if len(paths) > 1}

import click

@click.command()
@click.argument('directory', type=click.Path(exists=True))
def main(directory: str):
    result = find_duplicate(directory)
    if not result:
        click.echo(success("No duplicates found."))
        return
    click.echo(warning(f"Found {len(result)} duplicate group(s):\n"))
    for hash, paths in result.items():
        click.echo(header(hash))
        for p in paths:
            click.echo(path(f" {p}"))
        click.echo("")

if __name__ == "__main__":
    main()