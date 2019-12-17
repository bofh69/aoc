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

def gen_transforms(nums):
    rank = len(nums)
    m = tuple(tuple(pattern[((c+1)//(r+1)) % len(pattern)] for c in range(rank)) for r in range(rank))
    return m

def multiply(nums, trans):
    rank = len(nums)
    temp = tuple(sum([nums[c]*trans[r][c] for c in range(rank)]) for r in range(rank))
    temp = tuple(int(str(n)[-1]) for n in temp)
    return temp


if len(sys.argv) != 2:
    raise Exception("Expected one argument")

nums = parse_file(sys.argv[1])
trans = gen_transforms(nums)

for phase in range(100):
    nums = multiply(nums, trans)
    print(nums)

print(nums)
