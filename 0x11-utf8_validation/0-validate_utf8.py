#!/usr/bin/python3
"""
utf8 validation
"""


def validUTF8(data):
    """validUTF8 function"""
    bytes = 0;
    for num in data:
        bin_rep = format(num, "#010b")[-8:]
        if byte == 0:
            for bit in bin_rep:
                if bit == "0":
                    break
                bytes += 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (bin_rep[0] == "1" and bin_rep[1] == "0"):
                return False
        bytes -= 1
    return bytes == 0
