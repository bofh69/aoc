#!/usr/bin/env python3

import sys

def read_file(file):
    file = open(file, "r")
    text = file.read()
    file.close()
    return text

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

inp = read_file(sys.argv[1])
inp = inp.split('\n')

width = len(inp[0])
height = len(inp) - 1

astroids = []

for y in range(height):
    for x in range(width):
        if inp[y][x] == '#':
            astroids.append((x, y))

blocking = dict()
count = dict()

def is_between(first, second, third):
    if third >= first:
        if second >= first and second <= third:
            return True
    else:
        if second <= first and second >= third:
            return True
    return False

def is_blocked(first, second):
    fx, fy = first
    sx, sy = second
    dx, dy = sx - fx, sy - fy

    if (first, second) in blocking:
        return blocking.get((first, second))

    for third in astroids:
        if third != first and third != second:
            tx, ty = third
            if is_between(fx, tx, sx) and is_between(fy, ty, sy):
                if sx - fx != 0:
                    if tx - fx == 0:
                        continue
                    delta1 = (sy - fy) / (sx - fx)
                    delta2 = (ty - fy) / (tx - fx)
                    if delta1 == delta2:
                        blocking[(first, second)] = True
                        blocking[(second, first)] = True
                        return True
                else:
                    if (ty - fy == 0) or (ty - fy == 0):
                        continue
                    delta1 = (sx - fx) / (sy - fy)
                    delta2 = (tx - fx) / (ty - fy)
                    if delta1 == delta2:
                        blocking[(first, second)] = True
                        blocking[(second, first)] = True
                        return True
    blocking[(first, second)] = False
    blocking[(second, first)] = False
    return False

for first in astroids:
    (fx, fy) = first
    c = 0
    for second in astroids:
        if first != second:
            if not is_blocked(first, second):
                c = c + 1
    count[first] = c

max = 0
monitor = (0,0)
for astroid in astroids:
    if count[astroid] > max:
        max = count[astroid]
        monitor = astroid

print(monitor, max)
