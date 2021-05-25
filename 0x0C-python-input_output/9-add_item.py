#!/usr/bin/python3
"""
json module
"""

save = __import__('7-save_to_json_file.py').save_to_json_file
load = __import__('8-load_from_json_file.py').load_from_json_file


filename = "add_item.json"
json_list = load_from_json_file(filename)
save_to_json_file(json_list, filename)
