import os
from os.path import getsize, join

import click

from utils.common import path

EXCLUDE_DIRS = {"__pycache__", ".venv", "venv", "node_modules", ".git"}


def get_tree_sizes(directory: str, max_depth: int | None = None):
    results = []
    base_depth = directory.rstrip(os.sep).count(os.sep)
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        dirs.sort()
        if max_depth is not None and root.count(os.sep) - base_depth >= max_depth:
            dirs[:] = []  # stop recursing deeper
            continue
        for file in sorted(files):
            filepath = join(root, file)
            size = getsize(filepath)
            results.append((filepath, size))
    return sorted(results, key=lambda x: x[1], reverse=True)


def format_size(size: int):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


@click.command()
@click.argument("directory", type=click.Path(exists=True))
@click.option(
    "--max-depth", default=None, type=int, help="Maximum directory depth to traverse."
)
def main(directory: str, max_depth: int | None):
    results = get_tree_sizes(directory, max_depth)
    for filepath, size in results:
        click.echo(f"{format_size(size)}  {path(filepath)}")


if __name__ == "__main__":
    main()
