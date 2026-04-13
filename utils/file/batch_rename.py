import os

from utils.common import success, warning, path

def batch_rename(directory: str, match: str, replace: str):
    matches = {}
    for root, dirs, files in os.walk(directory):
        dirs.sort()
        for file in sorted(files):
            filepath = os.path.join(root, file)
            new_name = file.replace(match, replace)
            if new_name == file:
                continue
            new_filepath = os.path.join(root, new_name)
            if os.path.exists(new_filepath):
                continue
            matches[filepath] = new_filepath
    return matches

def apply_renames(matches: dict, dry_run: bool = False):
    for src, dst in matches.items():
        if dry_run:
            click.echo(f"{path(src)} → {warning(dst)}")
        else:
            os.rename(src, dst)
            click.echo(success(f"Renamed: {src} → {dst}"))

import click

@click.command()
@click.option('--dry-run', is_flag=True, help="Show what would be renamed without doing it.")
@click.argument('directory', type=click.Path(exists=True))
@click.argument('match', type=click.STRING)
@click.argument('replace', type=click.STRING)
def main(directory: str, match: str, replace: str, dry_run: bool):
    matches = batch_rename(directory, match, replace)
    if not matches:
        click.echo("No files matched.")
        return
    apply_renames(matches, dry_run=dry_run)

if __name__ == "__main__":
    main()
    