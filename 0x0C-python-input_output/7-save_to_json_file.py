#!/usr/bin/python3
"""
save to json file module
"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file fct"""
    with open(filename, mode = "w", encoding="utf-8") as file:
        file.write(json.dump(my_object))
