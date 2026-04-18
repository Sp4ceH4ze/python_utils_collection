import sys

import click

from utils.common import error, header, success, warning
from utils.text.patterns import PATTERNS


PATTERN_CATEGORIES = {
    "Web": ["url", "email", "user_agent", "html_tag", "html_comment", "css_color_hex", "css_color_rgb"],
    "Network": ["ipv4", "ipv6", "cidr", "port", "mac_address"],
    "Security": ["jwt", "bearer_token", "api_key", "aws_key", "private_key_header", "base64", "password_in_url", "connection_string"],
    "Dev & Infra": ["uuid", "semver", "git_commit", "docker_image", "env_variable", "filepath_unix", "filepath_windows", "python_import", "shebang"],
    "Date & Time": ["date", "time", "iso8601", "unix_timestamp"],
    "Finance": ["credit_card", "iban", "btc_address", "eth_address", "price"],
    "Identity": ["phone", "ssn", "passport", "postal_code", "coordinates"],
    "Social": ["hashtag", "mention"],
    "Logs": ["log_level", "http_method", "http_status", "log_timestamp", "stack_trace"],
}


def extract(text: str, pattern: str):
    if pattern not in PATTERNS:
        raise ValueError(f"Unknown pattern '{pattern}'. Available: {list(PATTERNS)}")
    return PATTERNS[pattern].findall(text)


def list_patterns():
    available = set(PATTERNS)
    for cat, items in PATTERN_CATEGORIES.items():
        click.echo(header(f"{cat}:"))
        for p in items:
            status = "" if p in available else " [missing]"
            prefix = "  " if p in available else "  !"
            click.echo(f"{prefix}{p}{status}")


def get_content(text: str | None, file: str | None):
    if file:
        with open(file) as f:
            return f.read()
    if text:
        return text
    return sys.stdin.read()


@click.command()
@click.argument("pattern", required=False)
@click.option("--text", help="Text to search")
@click.option("--file", type=click.Path(exists=True), help="File to search")
@click.option("-l", "--list", "show_list", is_flag=True, help="List available patterns")
@click.option("--unique/--no-unique", default=True, help="Deduplicate results")
def main(pattern, text, file, show_list, unique):
    if show_list:
        click.echo(header("Available Patterns:\n"))
        list_patterns()
        return

    if not pattern:
        click.echo(error("Provide a pattern name. Use --list to see available."))
        return

    content = get_content(text, file)

    try:
        results = extract(content, pattern)
    except ValueError as e:
        click.echo(error(str(e)))
        return

    if unique:
        results = list(dict.fromkeys(results))

    if not results:
        click.echo(warning("No matches found."))
        return

    for r in results:
        click.echo(success(r))


if __name__ == "__main__":
    main()