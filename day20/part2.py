#!/usr/bin/env python3

import sys
import math
import re

def read_file(file):
    file = open(file, "r")
    text = file.read()
    file.close()
    return text

def add_portal(rows, pos, pos1, pos2, portals):
    if rows[pos1[1]][pos1[0]].isalpha() and rows[pos2[1]][pos2[0]].isalpha():
        name = rows[pos1[1]][pos1[0]] + rows[pos2[1]][pos2[0]]
        portals[0][pos] = name
        if name in portals[1]:
            portals[1][name].append(pos)
        else:
            portals[1][name] = [pos]

def north(pos):
    return (pos[0], pos[1]-1)

def south(pos):
    return (pos[0], pos[1]+1)

def east(pos):
    return (pos[0]+1, pos[1])

def west(pos):
    return (pos[0]-1, pos[1])

def neighbor(nodes, pos):
    if north(pos) in nodes:
        return north(pos)
    if south(pos) in nodes:
        return south(pos)
    if east(pos) in nodes:
        return east(pos)
    if west(pos) in nodes:
        return west(pos)
    raise Exception("No neightbor!")

def in_or_out(pos, min_x, max_x, min_y, max_y):
    (x, y) = pos
    if x < min_x or x > max_x or y < min_y or y > max_y:
        return 'I'
    else:
        return 'O'

def parse_file(file):
    inp = read_file(file)
    rows = []
    row = []
    for y, s in enumerate(inp.split('\n')):
        for c in s:
            row.append(c)
        rows.append(row)
        row = []
    # pos -> name, name -> [pos]
    portals = (dict(), dict())
    nodes = dict()
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c == '.':
                nodes[(x, y)] = []
                add_portal(rows, (x, y-1), (x, y-2), (x, y-1), portals)
                add_portal(rows, (x, y+1), (x, y+1), (x, y+2), portals)
                add_portal(rows, (x-1, y), (x-2, y), (x-1, y), portals)
                add_portal(rows, (x+1, y), (x+1, y), (x+2, y), portals)
    for pos, node in nodes.items():
        if north(pos) in nodes:
            node.append((north(pos), 'N'))
        if south(pos) in nodes:
            node.append((south(pos), 'S'))
        if east(pos) in nodes:
            node.append((east(pos), 'E'))
        if west(pos) in nodes:
            node.append((west(pos), 'W'))
            
    min_x = 100000
    min_y = 100000
    max_x = 0
    max_y = 0
    for pos in nodes.keys():
        (x, y) = pos
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    for name, pos in portals[1].items():
        if name != 'AA' and name != 'ZZ':
            n1 = neighbor(nodes, pos[0])
            n2 = neighbor(nodes, pos[1])
            print(name, n1, n2)
            nodes[n1].append((n2, in_or_out(pos[0], min_x, max_x, min_y, max_y)))
            nodes[n2].append((n1, in_or_out(pos[1], min_x, max_x, min_y, max_y)))
    return (nodes,
            neighbor(nodes, portals[1]['AA'][0]),
            neighbor(nodes, portals[1]['ZZ'][0]),
            portals)

def bfs(graph, start, goal):
    visited = dict()
    to_explore = [((start, 0), 0, "")]
    while len(to_explore) > 0:
        ((pos, depth), length, path) = to_explore[0]
        if depth == 0 and pos == goal:
            return (length, path)
        to_explore = to_explore[1::]
        if not (pos, depth) in visited:
            # print("Trying", pos, depth, path, graph[pos])
            visited[(pos, depth)] = True
            for (new_pos, d) in graph[pos]:
                if not (new_pos, depth) in visited:
                    if d == 'I':
                        depth = depth + 1
                    elif d == 'O':
                        depth = depth - 1
                    if d != 'I' or depth > 0:
                        to_explore.append(((new_pos, depth), length+1, path + d))
    raise Exception("No path to goal")



if len(sys.argv) != 2:
    raise Exception("Expected one argument")

(graph, start, goal, portals) = parse_file(sys.argv[1])

# for y in range(38):
    # for x in range(60):
        # p = (x, y)
        # if p in portals[0]:
            # sys.stdout.write('*')
        # elif p in graph:
            # sys.stdout.write('.')
        # else:
            # sys.stdout.write(' ')
    # print()

# print(start, goal)

(length, path) = bfs(graph, start, goal)

print(length, path)
