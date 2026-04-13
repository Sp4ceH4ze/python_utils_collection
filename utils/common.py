import click

common_options = lambda f: (
    click.option("--verbose", is_flag=True)(
    click.option("--format", type=click.Choice(["json", "table"]), default="table")(
    click.option("--output", type=click.Path())(f)))
)