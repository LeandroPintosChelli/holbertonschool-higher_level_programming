#!/usr/bin/python3
"""Adds all arguments to a Python list,
and then save them to a file."""


import sys


import json


save = __import__('5-save_to_json_file').save_to_json_file


load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    file = []
    try:
        file = load('add_item.json')
    except:
        pass
    for txt in range(1, len(sys.argv)):
        txt.append(sys.argv[i])
    save(txt, 'add_item.json')