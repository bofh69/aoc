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

def print_map(num, depth):
    if num == 0:
        return
    print("Depth %d:" % depth)
    for y in range(5):
        for x in range(5):
            if x == 2 and y == 2:
                sys.stdout.write('?')
            elif num & 2**(x + y*5) != 0:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        print()
    print()

def count_col(num, col):
    c = 0
    for y in range(5):
        if (num & int(2**(col + y*5))) != 0:
            c = c + 1
    return c

def count_row(num, row):
    c = 0
    for x in range(5):
        if (num & int(2**(x + row*5))) != 0:
            c = c + 1
    return c

def count_neighbours(nums, depth, x, y):
    c = 0

    num = nums[depth]

    # 0 1 ? 3 4
    if x == 0:
        if 0 != (nums[depth-1] & int(2**(1 + 2*5))):
            # One step out, (1,2) position
            c = c + 1
    elif y == 2 and x == 3:
        # One step down, right column
        c = c + count_col(nums[depth+1], 4)
    elif x > 0 and 0 != num & int(2**(x-1 + y * 5)):
        c = c + 1

    if x == 4:
        if 0 != (nums[depth-1] & int(2**(3 + 2*5))):
            # One step out, (3,2) position
            c = c + 1
    elif y == 2 and x == 1:
        # One step down, left column
        c = c + count_col(nums[depth+1], 0)
    elif x < 4 and (0 != (num & int(2**(x+1 + y * 5)))):
        c = c + 1

    if y == 0:
        if 0 != (nums[depth-1] & int(2**(2 + 1*5))):
            # One step out, (2,1) position
            c = c + 1
    elif x == 2 and y == 3:
        # One step down, bottom row
        c = c + count_row(nums[depth+1], 4)
    elif y > 0 and 0 != num & int(2**(x + (y-1) * 5)):
        c = c + 1

    if y == 4:
        if 0 != (nums[depth-1] & int(2**(2 + 3*5))):
            # One step out, (2,3) position
            c = c + 1
    elif x == 2 and y == 1:
        # One step down, top row
        c = c + count_row(nums[depth+1], 0)
    elif (y < 4) and 0 != (num & int(2**(x + (y+1) * 5))):
        c = c + 1

    return c

def update(nums, new_nums, depth):
    new_num = 0
    num = nums[depth]

    for y in range(5):
        for x in range(5):
            if x == 2 and y == 2:
                pass
            else:
                if (num & int(2**(x + y*5))) != 0:
                    c = count_neighbours(nums, depth, x, y)
                    if c == 1:
                        new_num = new_num | int(2**(x + y*5))
                else:
                    c = count_neighbours(nums, depth, x, y)
                    if c == 1 or c == 2:
                        new_num = new_num | int(2**(x + y*5))
    new_nums[depth] = new_num

def count_bits(num):
    c = 0
    for i in range(25):
        if num & int(2**i) != 0:
            c = c + 1
    return c

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

init_map = parse_file(sys.argv[1])

MIDDLE = 501
nums = [0 for x in range(MIDDLE*2+1)]
nums = [nums, nums.copy()]

cur = 0
nums[cur][MIDDLE] = init_map

for gen in range(200):
    next_cur = (cur+1) % 2
    for depth in range(MIDDLE-gen-1, MIDDLE+gen+2):
        update(nums[cur], nums[next_cur], depth)
    cur = next_cur

c = 0
for num in nums[cur]:
    c = c + count_bits(num)

for depth in range(MIDDLE-10, MIDDLE+10):
    print_map(nums[cur][depth], depth-MIDDLE)

print(c)
