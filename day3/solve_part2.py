#!/usr/bin/env python3

import sys

def read_path(file):
    file = open(file, "r")
    text = file.read()
    file.close()
    return text

def make_right(l, x, y, dist, result):
    for i in range(l):
        result[(x, y)] = dist
        x = x + 1
        dist = dist + 1
    return (x, y, dist)

def make_left(l, x, y, dist, result):
    for i in range(l):
        result[(x, y)] = dist
        x = x - 1
        dist = dist + 1
    return (x, y, dist)

def make_up(l, x, y, dist, result):
    for i in range(l):
        result[(x, y)] = dist
        y = y + 1
        dist = dist + 1
    return (x, y, dist)

def make_down(l, x, y, dist, result):
    for i in range(l):
        result[(x, y)] = dist
        y = y - 1
        dist = dist + 1
    return (x, y, dist)

def make_line(path, x, y, dist, result):
    dir = path[0]
    l = int(path[1:])
    if dir == 'R':
        ret = make_right(l, x, y, dist, result)
    elif dir == 'L':
        ret = make_left(l, x, y, dist, result)
    elif dir == 'U':
        ret = make_up(l, x, y, dist, result)
    elif dir == 'D':
        ret = make_down(l, x, y, dist, result)
    return ret


def parse_line(line):
    line = line.split(',')
    result = dict()
    x, y, dist = 0, 0, 0
    for path in line:
        (x, y, dist) = make_line(path, x, y, dist, result)
    return result

if len(sys.argv) != 2:
    print("Usage: %s <input>" % sys.argv[0])
    sys.exit(1)

input = read_path(sys.argv[1])
input = input.split('\n')

wire1 = parse_line(input[0])
wire2 = parse_line(input[1])

min_dist = 99999999
pos = (0, 0)
for ((x, y), dist1) in wire1.items():
    dist2 =  wire2.get((x, y), 0)
    if dist2 > 0:
        dist = dist1 + dist2

        if dist < min_dist:
            min_dist = dist
            pos = (x,y)

print(min_dist)
