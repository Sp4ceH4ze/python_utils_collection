import secrets
import string

import click

from utils.common import success


def set_alphabet(include_special: bool):
    if not include_special:
        alphabet = string.ascii_letters + string.digits
    else:
        alphabet = string.ascii_letters + string.digits + string.punctuation
    return alphabet


def gen_password(length: int = 16, include_special: bool = False):
    """Generate random password. Default: no special characters."""
    if include_special:
        abc = string.ascii_letters + string.digits + string.punctuation
    else:
        abc = string.ascii_letters + string.digits
    return "".join(secrets.choice(abc) for _ in range(length))


@click.command()
@click.option("--length", default=16)
@click.option("--count", default=1)
@click.option("--symbols", is_flag=True)
def main(length: int, count: int, symbols: bool):
    for _ in range(count):
        click.echo(success(gen_password(length, include_special=symbols)))


if __name__ == "__main__":
    main()
