#!/usr/bin/env python3

import sys

def read_file(file):
    file = open(file, "r")
    text = file.read()
    file.close()
    return text

nodes = []
edges = dict()

def parse_input(file):
    for line in read_file(file).split('\n'):
        data = line.split(')')
        if len(data) == 1:
            continue
        if len(data) != 2:
            raise Exception("Expected x)y: %s (%d)" % (line, len(data)))
        if not data[0] in nodes:
            nodes.append(data[0])
        if not data[1] in nodes:
            nodes.append(data[1])
        edges[data[1]] = data[0]

depth = dict()
depth['COM'] = 0

def count_orbits(node):
    if node == 'COM':
        return 0
    if not node in depth:
        depth[node] = 1 + count_orbits(edges[node])
    return depth[node]

def count_it():
    count = 0
    for n in nodes:
        count = count + count_orbits(n)
    return count

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

parse_input(sys.argv[1])


print("Nodes:", nodes)
print("Edges:", edges)
print("Result:", count_it())
