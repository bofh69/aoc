#!/usr/bin/env python3

import sys
import math

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

# Modified to give a theta where 0 is up, pi/2 right:
def polar(x, y):
    r = (x*x + y*y) ** 0.5
    t = math.atan2(x, y)
    if t < 0:
        t = t + 2*math.pi
    return (r, t)

max = 0
monitor = (8,3)
if True:
    for first in astroids:
        (fx, fy) = first
        c = 0
        for second in astroids:
            if first != second:
                if not is_blocked(first, second):
                    c = c + 1
        count[first] = c

    max = 0
    monitor = (11,13)
    for astroid in astroids:
        if count[astroid] > max:
            max = count[astroid]
            monitor = astroid

print(monitor, max)

coordinates = dict()

for astroid in astroids:
    if astroid != monitor:
        ax, ay = astroid
        mx, my = monitor
        (r, t) = polar(ax-mx, my-ay)
        arr = coordinates.setdefault(t, [])
        arr.append((astroid, r))

for theta in coordinates:
    coordinates[theta].sort(key=lambda entry: entry[1])

shotdown = dict()
count = 0

coords = sorted(coordinates.keys())

for theta in coords:
    arr = coordinates[theta]
    done = False
    for coord in arr:
        if not done:
            (astroid, r) = coord
            if not astroid in shotdown:
                shotdown[astroid] = True
                count = count + 1
                (x, y) = astroid
                print("The %d astroid is " % count, astroid, x * 100 + y)
                done = True
