import os
import click
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

from utils.common import success, path, dry_run_option

load_dotenv()

TARGET_DIR = Path(os.getenv("TRASH_DIR", "~/.local/share/Trash/files/")).expanduser()

def safe_delete(filepath: str):
    src = Path(filepath)
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    dst = TARGET_DIR / f"{src.stem}_{timestamp}{src.suffix}"
    src.move(dst)
    return dst

@click.command()
@dry_run_option
@click.argument('files', type=click.Path(exists=True), nargs=-1, required=True)
def main(files, dry_run):
    for file in files:
        if dry_run:
            click.echo(f"Would trash: {path(file)}")
        else:
            dst = safe_delete(file)
            click.echo(success(f"Moved to trash: {path(str(dst))}"))

if __name__ == "__main__":
    main()
