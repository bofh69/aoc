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
            node.append(north(pos))
        if south(pos) in nodes:
            node.append(south(pos))
        if east(pos) in nodes:
            node.append(east(pos))
        if west(pos) in nodes:
            node.append(west(pos))
            
    for name, pos in portals[1].items():
        if name != 'AA' and name != 'ZZ':
            n1 = neighbor(nodes, pos[0])
            n2 = neighbor(nodes, pos[1])
            nodes[n1].append(n2)
            nodes[n2].append(n1)
    return (nodes,
            neighbor(nodes, portals[1]['AA'][0]),
            neighbor(nodes, portals[1]['ZZ'][0]),
            portals)

def add_to_explore(pos, length, d, path, graph, visited, to_explore):
    if pos in graph:
        if not pos in visited:
            to_explore.append((pos, length+1, path+d))

def bfs(graph, start, goal):
    visited = dict()
    to_explore = [(start, 0, "")]
    while len(to_explore) > 0:
        (pos, length, path) = to_explore[0]
        if pos == goal:
            return (length, path)
        to_explore = to_explore[1::]
        if not pos in visited:
            print("Trying", pos, graph[pos])
            visited[pos] = True
            for new_pos in graph[pos]:
                if not new_pos in visited:
                    to_explore.append((new_pos, length+1, "?"))
    raise Exception("No path to goal")



if len(sys.argv) != 2:
    raise Exception("Expected one argument")

(graph, start, goal, portals) = parse_file(sys.argv[1])

for y in range(38):
    for x in range(60):
        p = (x, y)
        if p in portals[0]:
            sys.stdout.write('*')
        elif p in graph:
            sys.stdout.write('.')
        else:
            sys.stdout.write(' ')
    print()

print(start, goal)

(length, path) = bfs(graph, start, goal)

print(length, path)
