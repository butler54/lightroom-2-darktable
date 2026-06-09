# SPDX-FileCopyrightText: 2025-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
"""Core CLI init using typer"""
import pathlib
import types
import typer


app = typer.Typer()


@app.callback()
def main(
    ctx: typer.Context, 
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
    catalogs: Optional[List[pathlib.Path]] = typer.Option(
        None,
        "--catalog",
        "-c",
        help= "Specify your .lrcat files",
    )
):
    """
    Main entry point for the CLI. Sets global options.
    """
    ctx.obj = types.SimpleNamespace(verbose=verbose, catalogs=catalogs or [])


# @app.command()
# def listcollections(
#     ctx: typer.Context,



# @app.command()
# def foo(
#     ctx: typer.Context,
#     force: bool = typer.Option(
#         False, "--force", "-f", help="Force the foo action"
#     ),
#     count: int = typer.Option(
#         1, "--count", "-c", help="Number of times to foo"
#     ),
# ):
#     """
#     Foo subcommand with its own flags.
#     """
#     if ctx.obj.verbose:
#         typer.echo(f"[VERBOSE] Running foo with force={force}, count={count}")
#     typer.echo(f"Foo called with tags: {ctx.obj.tag}")
#     typer.echo(f"Force: {force}, Count: {count}")

# @app.command()
# def bar(
#     ctx: typer.Context,
#     dry_run: bool = typer.Option(
#         False, "--dry-run", help="Do a dry run of bar"
#     ),
#     level: str = typer.Option(
#         "info", "--level", "-l", help="Set the bar level"
#     ),
# ):
#     """
#     Bar subcommand with its own flags.
#     """
#     if ctx.obj.verbose:
#         typer.echo(f"[VERBOSE] Running bar with dry_run={dry_run}, level={level}")
#     typer.echo(f"Bar called with tags: {ctx.obj.tag}")
#     typer.echo(f"Dry run: {dry_run}, Level: {level}")





def cli():
    app()