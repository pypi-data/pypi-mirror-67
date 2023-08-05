
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


@app.command("storage")
def storage():
    api = from_env()
    store = api.store
    typer.echo(cyan(f"Store: name={store.NAME} path={store.path}"))
    done()


@app.command("add")
def add_(path: str):
    api = from_env()

    typer.echo(cyan(f"Reading: {path}"))
    dataset = api.read(path)
    typer.echo(cyan(f"Found: {len(dataset)}"))

    contacts = api.add(dataset)

    render_contacts(contacts, prefix=green("Added: "))
    done()


@app.command("get")
def get(ids: List[str] = typer.Argument(None), fmt: str = typer.Option("json")):
    api = from_env()
    items = api.get(list(ids))
    dataset = [i.dict() for i in items]
    text = api.dumps(dataset, fmt=fmt)
    typer.echo(text)


@app.command("remove")
def remove(ids: List[str]):
    api = from_env()
    contacts = api.remove(list(ids))

    render_contacts(contacts, prefix=green("Removed: "))
    done()


@app.command("clear")
def clear():
    api = from_env()
    api.clear()
    typer.echo(f"Removed all contacts!")
    done()


def render_contacts(contacts, prefix=""):
    for contact in contacts:
        text = f"{prefix}name={contact.name} id={contact.id}"
        typer.echo(text)


def cyan(msg: str) -> str:
    return typer.style(msg, fg=typer.colors.BRIGHT_CYAN)


def green(msg: str) -> str:
    return typer.style(msg, fg=typer.colors.BRIGHT_GREEN)


def done(msg="Complete!"):
    text = typer.style(msg, fg=typer.colors.BRIGHT_WHITE, bold=True)
    typer.echo(text)