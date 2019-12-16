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

def update_velocity(velocity, moon, moons):
    for second in moons:
        for d in range(3):
            if moon[d] < second[d]:
                velocity[d] = velocity[d] + 1
            if moon[d] > second[d]:
                velocity[d] = velocity[d] - 1
    return velocity

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

positions = parse_file(sys.argv[1])
velocities = []
for x in range(len(positions)):
    velocities.append([0,0,0])
n_moons = len(positions)

old_positions = []
for idx in range(n_moons):
    old_positions.append(dict())

for step in range((4686774924+1)//1000):
    for idx in range(n_moons):
        velocities[idx] = update_velocity(velocities[idx], positions[idx], positions)
    for idx in range(n_moons):
        for d in range(3):
            positions[idx][d] = positions[idx][d] + velocities[idx][d]
        key = (positions[idx][0],
               positions[idx][1],
               positions[idx][2],
               velocities[idx][0],
               velocities[idx][1],
               velocities[idx][2])
        if key in old_positions[idx]:
            #print(idx, step, old_positions[idx][key])
            pass
        else:
            old_positions[idx][key] = step
