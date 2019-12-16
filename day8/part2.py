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

image = ['2'] * ppl;

print("Layers", layers)

for l in range(layers):
    for y in range(height):
        for x in range(width):
            pos = x + y * width
            idx = ppl*l + pos
            c = data[idx]
            if c != '2':
                if image[pos] == '2':
                    image[pos] = c
                    sys.stdout.write(c)
print()

for y in range(height):
    for x in range(width):
        pos = x + y * width
        c = image[pos]
        if c == '1':
            sys.stdout.write('#')
        elif c == '0':
            sys.stdout.write('.')
        elif c == '2':
            sys.stdout.write(' ')
        else:
            sys.stdout.write('?')
    print()
