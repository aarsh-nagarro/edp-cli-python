# edp_cli.py

import typer

app = typer.Typer()

@app.command(name="say-hello")
def say_hello(name: str = typer.Option(..., help="Name of the person to greet")):
    """
    Greet someone with hello.
    """
    typer.echo(f"Hello, {name}! 👋")

@app.command(name="say-bye")
def say_bye(name: str = typer.Option(..., help="Name of the person to bid farewell")):
    """
    Say goodbye to someone.
    """
    typer.echo(f"Goodbye, {name}! 👋")

# Future commands will be added here
# @app.command()
# def scaffold(...):
#     pass

# @app.command()
# def create_repo(...):
#     pass

if __name__ == "__main__":
    app()
