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

def find_dist(node, parent, depth=dict()):
    if node == parent:
        return 0
    if not node in depth:
        depth[node] = 1 + find_dist(edges[node], parent, depth)
    return depth[node]

def get_parent(node, parents):
    if node in parents:
        return node
    parents.append(node)
    return get_parent(edges[node], parents)

def find_common_parent(node1, node2):
    parents = ['COM']
    get_parent(edges[node1], parents)
    p2 = get_parent(edges[node2], parents)
    return p2

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

parse_input(sys.argv[1])

parent = find_common_parent('YOU', 'SAN')
print("Parent: ", parent)
d1 = find_dist(edges['YOU'], parent)
print("d1: ", d1)
d2 = find_dist(edges['SAN'], parent)
print("d2: ", d2)

print("Result:", d1 + d2)
