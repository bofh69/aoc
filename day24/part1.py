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
    num = 0
    for y, s in enumerate(inp.split('\n')[:-1]):
        for (x, c) in enumerate(s):
            if c == '#':
                num = num | int(2**(x + y*5))
    return num

def print_map(num):
    for y in range(5):
        for x in range(5):
            if num & 2**(x + y*5) != 0:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        print()

def count_neighbours(num, x, y):
    c = 0
    if x > 0 and 0 != num & int(2**(x-1 + y * 5)):
        c = c + 1
    if x < 4 and 0 != num & int(2**(x+1 + y * 5)):
        c = c + 1
    if y > 0 and 0 != num & int(2**(x + (y-1) * 5)):
        c = c + 1
    if y < 4 and 0 != num & int(2**(x + (y+1) * 5)):
        c = c + 1
    return c

def update(num):
    new_num = 0

    for y in range(5):
        for x in range(5):
            if num & int(2**(x + y*5)) != 0:
                c = count_neighbours(num, x, y)
                if c == 1:
                    new_num = new_num | int(2**(x + y*5))
            else:
                c = count_neighbours(num, x, y)
                if c == 1 or c == 2:
                    new_num = new_num | int(2**(x + y*5))
    return new_num

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

current_map = parse_file(sys.argv[1])

old_values = dict()

while not current_map in old_values:
    old_values[current_map] = True
    current_map = update(current_map)

print_map(current_map)
print(current_map)

