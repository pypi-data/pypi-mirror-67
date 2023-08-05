
import json
import typer
from typing import List

from . import from_env


app = typer.Typer()


@app.command("formats")
def formats():
    api = from_env()
    formats = api.get_formats()
    output = json.dumps(formats, indent=2)
    typer.echo(output)


@app.command("put")
def put_file(path: str):
    api = from_env()
    items = api.put_file(path)
    count = len(items)
    if count > 1:
        typer.echo(info(f"Created {count} new items"))
    else:
        typer.echo(info(f"Created new item"))

    for item in items:
        typer.echo(f"id={item.id} name={item.name}")


@app.command("get")
def get_text(ids: List[str] = typer.Argument(None), fmt: str = typer.Option("json")):
    api = from_env()
    text = api.get_text(list(ids), fmt=fmt)
    typer.echo(text)


@app.command("clear")
def clear():
    api = from_env()
    api.store.clear()
    typer.echo(info("Cleared all items!"))


def info(msg: str) -> str:
    """
    Info

    Format the given string as an info message.
    """
    return typer.style(msg, fg=typer.colors.BRIGHT_YELLOW, bold=True)
