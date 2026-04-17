import os
import click
import hashlib

from utils.common import success, error

def hash_string(text: str, algorithm: str):
    h = hashlib.new(algorithm)
    h.update(text.encode())
    return h.hexdigest()

def hash_file(path: str, algorithm: str):
    with open(path, "rb") as f:
        digest = hashlib.file_digest(f, algorithm)
    return digest.hexdigest()

def hash_directory(path: str, algorithm: str):
    h = hashlib.new(algorithm)
    for root, dirs, files in os.walk(path):
        dirs.sort()
        for file in sorted(files):
            filepath = os.path.join(root, file)
            h.update(hash_file(filepath, algorithm).encode())
    return h.hexdigest()

def hash_compare(result: str, expected: str):
    return result == expected, result

@click.group()
def main():
    pass

@main.command()
@click.option('--check', default=None, metavar='HASH', help="Checksum to verify against.")
@click.argument('path', type=click.Path(exists=True))
@click.argument('algorithm', type=click.STRING)
def file(path, algorithm, check):
    result = hash_directory(path, algorithm) if os.path.isdir(path) else hash_file(path, algorithm)
    if check:
        match, result = hash_compare(result, check)
        if match:
            click.echo(success("PASS  " + result))
        else:
            click.echo(error("FAIL"))
            click.echo(f"  expected: {check}")
            click.echo(f"  got:      {result}")
    else:
        print(result)

@main.command("string")
@click.option('--check', default=None, metavar='HASH', help="Checksum to verify against.")
@click.argument('text', type=click.STRING)
@click.argument('algorithm', type=click.STRING)
def hash_str(text, algorithm, check):
    result = hash_string(text, algorithm)
    if check:
        match, result = hash_compare(result, check)
        if match:
            click.echo(success("PASS  " + result))
        else:
            click.echo(error("FAIL"))
            click.echo(f"  expected: {check}")
            click.echo(f"  got:      {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()
    