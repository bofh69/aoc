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

for step in range(1000):
    print("After step: ", step+1)
    for idx in range(n_moons):
        velocities[idx] = update_velocity(velocities[idx], positions[idx], positions)
    for idx in range(n_moons):
        for d in range(3):
            positions[idx][d] = positions[idx][d] + velocities[idx][d]
    energy = 0
    for idx in range(n_moons):
        pot = 0
        kin = 0
        for d in range(3):
            pot = pot + abs(positions[idx][d]) 
            kin = kin + abs(velocities[idx][d])
        energy = energy + pot * kin
        # print("Pos:", positions[idx], "Vel:", velocities[idx])
    print("Energy: ", energy)
