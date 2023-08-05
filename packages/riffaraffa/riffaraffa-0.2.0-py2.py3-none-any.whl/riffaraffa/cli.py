#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import time

import click

from .riffaraffa import Movies


@click.group()
@click.version_option()
@click.pass_context
def main(ctx):
    """ Console script for riffaraffa. """
    ctx.obj = Movies()

    return 0


@main.command()
@click.argument("movie")
@click.pass_obj
def add(ctx, movie):
    """ Add a movie to the database. """
    click.echo("Adding {} to the database... ".format(movie), nl=False)
    ctx.add(movie)
    click.echo("Done.")


@main.command()
@click.pass_obj
def choose(ctx):
    """ Choose a movie from the list. """
    click.echo("La riffa e la raffa begins!\n")
    click.echo("Rullo di tamburi...", nl=False)
    for _ in range(10):
        click.echo(".", nl=False)
        time.sleep(0.2)
    click.echo("\n")

    movie = ctx.choose()
    click.echo("And the winner is:\n")
    click.echo("\t{}\n".format(movie.name))
    if click.confirm("Are you sure you want to watch this movie?"):
        ctx.watch(movie.id)


@main.command()
@click.pass_obj
def show(ctx):
    """ Show available movies from the database. """
    click.echo("Available movies: \n")
    ctx.show()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
