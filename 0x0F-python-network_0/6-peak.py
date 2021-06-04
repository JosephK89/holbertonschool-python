#!/usr/bin/python3
"""
find peak module
"""


def find_peak(list_of_integers):
    """find_peak fct."""
    if not list_of_integers:
        return None
    start = 0
    l = len(list_of_integers)
    end = len(list_of_integers) - 1
    mid = (start + end) / 2
    mid = int(mid)
    if l == 1:
        return list_of_integers[0]
    if l == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid -1]:
        return find_peak(list_of_integers[:mid])
