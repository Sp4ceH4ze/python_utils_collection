# Patterns sourced from gitleaks (https://github.com/gitleaks/gitleaks)
# Licensed under MIT License — see LICENSES/gitleaks-MIT.md

import os
import regex as re
import tomllib

from utils.common import success, warning, header, path

GITLEAKS_TOML = os.path.join(os.path.dirname(__file__), "rules/gitleaks.toml")

with open(GITLEAKS_TOML, "rb") as f:
    config = tomllib.load(f)

rules = config["rules"]
allowlist = config.get("allowlist", {})
ignored_paths = allowlist.get("paths", [])

compiled_rules = []
for rule in rules:
    if "regex" not in rule:
        continue
    try:
        compiled_rules.append({
            "id": rule["id"],
            "description": rule["description"],
            "pattern": re.compile(rule["regex"])
        })
    except re.error:
        pass

def scan(directory: str):
    matches = []
    for root, dirs, files in os.walk(directory):
        dirs.sort()
        for file in sorted (files):
            filepath = os.path.join(root, file)
            if any(re.search(pattern, filepath) for pattern in ignored_paths):
                continue
            with open(filepath, 'r', errors="ignore") as f:
                for line_num, line in enumerate(f, start=1):
                    for rule in compiled_rules:
                        match = rule["pattern"].search(line)
                        if match:
                            matches.append({
                                "file": filepath,
                                "line": line_num,
                                "rule": rule["id"],
                                "match": match.group()
                            })
    return matches

import click

@click.command()
@click.argument('directory', type=click.Path(exists=True))
def main(directory: str):
    result = scan(directory)
    if not result:
        click.echo(success("No secrets founds."))
        return
    click.echo(header(f"Found {len(result)} secret(s):\n"))
    for item in result:
        click.echo(path(item['file']))
        click.echo(warning(f"line: {item['line']}\nrule: {item['rule']}\nmatch: {item['match']}"))
        click.echo("")

if __name__ == "__main__":
    main()
