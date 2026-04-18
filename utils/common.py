import click

# common_options = lambda f: (
#     click.option("--verbose", is_flag=True)(
#     click.option("--format", type=click.Choice(["json", "table"]), default="table")(
#     click.option("--output", type=click.Path())(f)))
# )


def dry_run_option(f):
    return click.option(
        "--dry-run", is_flag=True, help="Preview changes without applying them."
    )(f)


def success(text: str):
    return click.style(text, fg="green")


def error(text: str):
    return click.style(text, fg="red")


def warning(text: str):
    return click.style(text, fg="yellow")


def path(text: str):
    return click.style(text, fg="cyan")


def header(text: str):
    return click.style(text, fg="white", bold=True)
