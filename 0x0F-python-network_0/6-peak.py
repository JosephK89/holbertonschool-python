#!/usr/bin/python3
"""
find peak module
"""


def find_peak(list_of_integers):
    """find_peak fct."""
    if not list_of_integers:
        return None
    start = 0
    end = len(list_of_integers) - 1
    mid = (start + end) / 2
    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid -1]:
        return find_peak(list_of_integers[:mid])
    
