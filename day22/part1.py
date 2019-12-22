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
    return inp.split('\n')

if len(sys.argv) != 4:
    raise Exception("Expected one argument")

n_cards = int(sys.argv[1])
cards = list(range(n_cards))
card = int(sys.argv[2])
orders = parse_file(sys.argv[3])

for order in orders:
    if order == "":
        pass
    elif order == "deal into new stack":
        cards.reverse()
        card = n_cards - card - 1
    elif order.find("cut ") == 0:
        n = int(order[4:])
        cards = cards[n:] + cards[:n]
        if card >= n:
            card = card - n
        else:
            card = card + (n_cards - n)
    elif order.find("deal with increment ") == 0:
        n = int(order[20:])
        new_cards = list(range(n_cards))
        for i in range(n_cards):
            new_cards[i*n % n_cards] = cards[i]
        cards = new_cards
        card = card * n % n_cards
    else:
        raise Exception("Unknown order", order)

print(cards)
print(card)
