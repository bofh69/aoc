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
    inp = inp.split('\n')
    result = []
    # format <x=-8, y=-10, z=0>
    matcher = re.compile("<x=(.*), y=(.*), z=(.*)>")
    for line in inp:
        m = matcher.match(line)
        if m:
            result.append([int(m.group(1)), int(m.group(2)), int(m.group(3))])

    return result

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

world=[]
world.append(([],[]))
world.append(([],[]))
world.append(([],[]))
n_moons = 0

for position in parse_file(sys.argv[1]):
    world[0][0].append(position[0])
    world[0][1].append(0)
    world[1][0].append(position[1])
    world[1][1].append(0)
    world[2][0].append(position[2])
    world[2][1].append(0)
    n_moons = n_moons + 1

# world[dimension][pos=0, vel=1][moon1, moon2, ...]

def update_velocity(dim):
    for m1_idx in range(n_moons):
        pos_moon_1 = dim[0][m1_idx]
        vel_moon_1 = dim[1][m1_idx]

        for m2_idx in range(n_moons):
            if pos_moon_1 < dim[0][m2_idx]:
                vel_moon_1 = vel_moon_1 + 1
            if pos_moon_1 > dim[0][m2_idx]:
                vel_moon_1 = vel_moon_1 - 1
        dim[1][m1_idx] = vel_moon_1

def update_position(dim):
    for idx in range(n_moons):
        dim[0][idx] = dim[0][idx] + dim[1][idx]

# periods[dimension][moon] = [(phase, period), ...]
periods = []
for d in range(3):
    dim = world[d]

    start_state = (
            dim[0][0],
            dim[0][1],
            dim[0][2],
            dim[0][3],
            dim[1][0],
            dim[1][1],
            dim[1][2],
            dim[1][3])

    for step in range(1000000000):
        update_velocity(dim)
        update_position(dim)
        new_state = (
                dim[0][0],
                dim[0][1],
                dim[0][2],
                dim[0][3],
                dim[1][0],
                dim[1][1],
                dim[1][2],
                dim[1][3])
        if start_state == new_state:
            periods.append(step+1)
            break

print(periods)

# Find LCD of periods
