#!/usr/bin/python3
"""
boxes module
"""


def canUnlockAll(boxes):
    """canunlock fct"""
    mykeys = [0]
    for key in mykeys:
        for i in boxes[key]:
            if i < len(boxes) and i not in mykeys:
                mykeys.append(i)
    if len(mykeys) == len(boxes):
        return True
    return False
