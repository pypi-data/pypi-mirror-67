#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import random

from .config import client
from .models import Movie


class Movies:
    """ Class representing all movies from the GSheet. """

    def __init__(self):
        self._sheet = client.open('Riffaraffa').sheet1
        self.movies = self._sheet.get_all_records()
        self.last_id = len(self.movies)

    @property
    def all(self):
        """ List all available movies.

        Returns:
            List(Movie)
        """
        return [Movie(movie) for movie in self.movies]

    def watch(self, movie_id: int):
        """ Set the given movie as watched.

        Args:
            movie_id: id of the movie to watch
        """
        movie = self.all[movie_id - 1]
        movie.watch(self._sheet)

    def choose(self):
        """ Randomly choose a movie to watch.

        Returns:
            Movie
        """
        movie = random.choice(self.all)
        while movie.watched:
            movie = random.choice(self.all)
        return movie

    def add(self, movie_name: str):
        """ Add a new movie to the GSheet.

        Args:
            movie_name: name of the movie
        """
        row = [self.last_id + 1, movie_name, "FALSE"]
        self._sheet.insert_row(row, self.last_id)
        self.last_id += 1

    def show(self):
        """ Print a list of all available movies. """
        for movie in self.all:
            click.echo(f"{movie.name} {'(watched)' if movie.watched else ''}")
