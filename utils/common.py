import click

common_options = lambda f: (
    click.option("--verbose", is_flag=True)(
    click.option("--format", type=click.Choice(["json", "table"]), default="table")(
    click.option("--output", type=click.Path())(f)))
)

def success(text): return click.style(text, fg="green")
def error(text):   return click.style(text, fg="red")
def warning(text): return click.style(text, fg="yellow")
def path(text):    return click.style(text, fg="cyan")
def header(text):  return click.style(text, fg="white", bold=True)