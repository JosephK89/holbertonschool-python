#!/usr/bin/python3
"""
json module
"""
import sys
import os.path

save = __import__('7-save_to_json_file.py').save_to_json_file
load = __import__('8-load_from_json_file.py').load_from_json_file

filename = "add_item.json"
list = []
if os.path.exists(filename) and os.path.getsize(my_file) > 0:
    list = load_from_json_file(filename)

save_to_json_file(list + sys,argv[1:], filename)
