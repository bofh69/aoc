#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

lines = [ s.strip().split(' => ') for s in lines]
lines = [ (s[0].split(', '), s[1]) for s in lines]
lines = [ (list(tuple(t.split(' ')) for t in s[0]), tuple(s[1].split(' '))) for s in lines]

# X => (n, [(C, n2)*])
rules = dict()
# C => n
current = dict()

for p, (n, r) in lines:
    if r in rules:
        raise Exception("Compound already in rules")
    p = [(c, int(n2)) for (n2, c) in p]
    rules[r] = (int(n), p)
    current[r] = 0

ore = 0

def create_n_x(n, x, prefix=""):
    global ore
    if x == 'ORE':
        print("%sConsuming %d %s" % (prefix, n, x))
        ore = ore + n
        return
    nx = current[x]
    if nx >= n:
        print("%sConsuming %d %s" % (prefix, n, x))
        current[x] = nx - n
        return
    if nx > 0:
        print("%sConsuming %d %s" % (prefix, n - nx, x))
        n = n - nx
        nx = 0
    (np, p) = rules[x]
    if np >= n:
        print("%sProducing: %d %s" % (prefix, np, x))
        # Create one of each in p
        for (x2, n2) in p:
            create_n_x(n2, x2, x + " " + prefix)
        print("%sConsuming: %d %s" % (prefix, n, x))
        current[x] = np - n
    else:
        n_batches = (n+np-1) // np
        print("%sProducing: %d %s" % (prefix, n_batches * np, x))
        for (x2, n2) in p:
            create_n_x(n_batches * n2, x2, x + " " + prefix)
        current[x] = n_batches * np - n
        print("%sConsuming: %d (of %d) %s" % (prefix, n, current[x], x))

print(rules)

create_n_x(7863863, 'FUEL')

print(ore)
