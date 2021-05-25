#!/usr/bin/python3
"""
load from json file module
"""
import json


def load_from_json_file(filename):
    """load_from_json_file fct"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
