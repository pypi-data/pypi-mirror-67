#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste


class Movie:
    """ Class representing a movie from the GSheet. """

    def __init__(self, entry):
        self.id = entry.get("Id")
        self.name = entry.get("Name")
        self.watched = self._is_watched(entry.get("Watched"))

    def watch(self, sheet):
        """ Set the watched attribute of the movie to True.

        Args:
            sheet: gspread instance to act on
        """
        self.watched = True
        sheet.update_cell(self.id + 1, 3, True)

    @staticmethod
    def _is_watched(watched_string):
        return watched_string == "TRUE"

    def __repr__(self):
        return """Movie(id={}, name={}, watched={})""".format(self.id,
                                                              self.name,
                                                              self.watched)
