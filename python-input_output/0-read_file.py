#!/usr/bin/python3
"""Reads a text file and prints."""


def read_file(filename=""):
    """Reads a filename and prints its contents to stdout."""

    with open(filename) as file:
        read_text = file.read()
        print(read_text, end="")
