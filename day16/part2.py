#!/usr/bin/env python3

import sys
import math
import re

def read_file(file):
    file = open(file, "r")
    text = file.read()
    file.close()
    return text

def parse_file(file):
    inp = read_file(file)
    return tuple(int(s) for s in inp.split('\n')[0])

pattern = [0, 1, 0, -1]

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

nums = parse_file(sys.argv[1])

nums = nums * 10000

offset = 0
for d in nums[0:7]:
    offset = offset * 10 + d

nums = nums[offset:]

result = list(nums)
rank = len(nums)

# (2, 3, 8, 4, 5, 6, 7, 8)

for r in range(100):
    for c_ in range(rank):
        c = rank - c_ - 1
        if c == rank - 1:
            result[c] = nums[c]
        else:
            result[c] = (result[c] + result[c+1]) % 10

print(result[0:8])
