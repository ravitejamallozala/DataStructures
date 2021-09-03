"""
Cognitive scale
Write a program to Validate an IPv4 Address.
According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four
decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1
"""

"""Solution Regex : ^(25[0-5]\.|2[0-4][0-9]\.|1?\d?\d\.){3}(25[0-5]|2[0-4][0-9]|1?\d?\d)$"""
import re
import math

def check_num(num):
    if num > 255 or num < 0:
        return False
    return True


def validate_ip(inp):
    if not inp:
        return False
    inp_arr = inp.split(".")
    if not len(inp_arr) == 4:
        return False
    print(inp_arr)
    for num in inp_arr:
        if not re.match(r"[0-9]", num):
            return False
        num = int(num)
        if not check_num(num):
            return False
    return True


inp = "1a72.16.254"
print(validate_ip(inp))