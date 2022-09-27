#!/usr/bin/python3
"""Counts number of lines in a file."""


def write_file(filename="", text=""):
    """Counts lines in filename."""

    count = 0

    with open(filename) as file:
        text = file.readlines()
        for line in text:
            count += 1

    return count
