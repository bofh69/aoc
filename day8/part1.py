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

width = int(inp[0])
height = int(inp[1])
data = inp[2]

ppl = width * height # Pixels per layer
layers = len(data) // ppl

digits = []
for l in range(layers):
    digits.append(dict())
    for x in range(width):
        for y in range(height):
            idx = ppl*l + x + y * width
            c = data[idx]
            digits[l][c] = digits[l].get(c, 0) + 1

min_zero = ppl
min_layer = -1
result = 0
for l in range(layers):
    zeros = digits[l].get('0', ppl)
    if zeros < min_zero:
        min_zero = zeros
        min_layer = l
        result = digits[l].get('1', -1) * digits[l].get('2', -1)

print(min_layer, result)
