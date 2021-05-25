#!/usr/bin/python3
"""
json module
"""
import sys

save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load(filename)
except:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save(json_list, filename)
