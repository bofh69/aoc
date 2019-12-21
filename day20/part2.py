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
        return 'O'
    else:
        return 'I'

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
            node.append((north(pos), 1))
        if south(pos) in nodes:
            node.append((south(pos), 1))
        if east(pos) in nodes:
            node.append((east(pos), 1))
        if west(pos) in nodes:
            node.append((west(pos), 1))
            
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
    portals = tuple((neighbor(nodes, pos), name + in_or_out(pos, min_x, max_x, min_y, max_y)) for pos, name in portals[0].items())

    return (nodes,
            portals)

def bfs(graph, start, goals):
    results = dict()
    visited = dict()
    to_explore = [(start, 0)]
    goals = dict(goals)

    while len(to_explore) > 0:
        (pos, cost) = to_explore[0]
        to_explore = to_explore[1::]
        if not pos in visited:
            # Skip Start -> Start by checking cost
            if cost > 0 and pos in goals:
                results[goals[pos]] = cost
            visited[pos] = True
            for (new_pos, new_cost) in graph[pos]:
                if not new_pos in visited:
                    to_explore.append((new_pos, cost + new_cost))
    results = list(results.items())
    results.sort(key=lambda g: g[1])
    return results

def bfs2(graph, start, goals):
    # name, cost
    results = dict()
    visited = dict()
    goals = dict(goals)
    to_explore = [(start, 0, 0, start)]

    while len(to_explore) > 0:
        (pos, depth, cost, path) = to_explore[0]
        to_explore = to_explore[1::]
        if depth > 0 and pos in goals:
            continue
        if not (pos, depth) in visited:
            if depth == 0 and pos in goals:
                results[pos] = (cost, path)
                break
            visited[(pos, depth)] = True
            for (new_pos, new_cost) in graph[pos]:
                if not new_pos in visited:
                    new_depth = 0
                    if new_pos[0:2] == pos[0:2]:
                        if new_pos[2] == 'O':
                            new_depth = 1
                        else:
                            new_depth = -1
                    if depth + new_depth >= 0 and depth < 1000:
                        to_explore.append((new_pos, depth + new_depth, cost + new_cost, "%s->%s(%d)" % (path, new_pos, depth + new_depth)))
    return results

if len(sys.argv) != 2:
    raise Exception("Expected one argument")

(graph, portals) = parse_file(sys.argv[1])

dist = dict()
for f in portals:
    dist[f[1]] = bfs(graph, f[0], portals)

# Add portal to portal edges
for (pos, name) in portals:
    if name[2] == 'I':
        dist[name[0:2]+"I"].insert(0, (name[0:2] + "O", 1))
        dist[name[0:2]+"O"].insert(0, (name[0:2] + "I", 1))

print(bfs2(dist, "AAO", [("ZZO", 0)]))
