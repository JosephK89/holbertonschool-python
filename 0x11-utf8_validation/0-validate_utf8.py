#!/usr/bin/python3
"""
utf8 validation
"""


def validUTF8(data):
    """validUTF8 function"""
    c = 0;
    for byte in data:
        if 128 <= byte <=191:
            if c == 0:
                return False
            c -= 1
        else:
            if c:
                return False
            if byte < 128:
                continue
            elif byte < 224:
                c = 1
            elif byte < 240:
                c = 2
            elif byte < 248:
                c = 3
            else:
                return False
    return c == 0
