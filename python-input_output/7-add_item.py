#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""
import sys

import json


save = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    load = []
try:
    load = load_from('add_item.json')
except:
    pass
for i in range (1, len(sys.argv)):
    load.append(sys.argv[i])
save(load, 'add_item.json')