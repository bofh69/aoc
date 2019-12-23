#!/usr/bin/env python3

import itertools
import sys

prog = [3,62,1001,62,11,10,109,2259,105,1,0,2187,1043,604,1333,1434,1898,977,775,1366,946,1793,1500,1595,713,1218,1962,1119,1865,744,1929,1463,1760,2121,907,1628,1564,1078,1694,2156,845,680,2092,1659,1148,808,876,2228,1830,1531,641,1993,1247,1284,1399,2024,1177,1729,571,2059,1008,0,0,0,0,0,0,0,0,0,0,0,0,3,64,1008,64,-1,62,1006,62,88,1006,61,170,1105,1,73,3,65,21002,64,1,1,21002,66,1,2,21101,0,105,0,1106,0,436,1201,1,-1,64,1007,64,0,62,1005,62,73,7,64,67,62,1006,62,73,1002,64,2,132,1,132,68,132,1002,0,1,62,1001,132,1,140,8,0,65,63,2,63,62,62,1005,62,73,1002,64,2,161,1,161,68,161,1102,1,1,0,1001,161,1,169,1001,65,0,0,1102,1,1,61,1101,0,0,63,7,63,67,62,1006,62,203,1002,63,2,194,1,68,194,194,1006,0,73,1001,63,1,63,1105,1,178,21101,210,0,0,105,1,69,2101,0,1,70,1101,0,0,63,7,63,71,62,1006,62,250,1002,63,2,234,1,72,234,234,4,0,101,1,234,240,4,0,4,70,1001,63,1,63,1106,0,218,1105,1,73,109,4,21101,0,0,-3,21101,0,0,-2,20207,-2,67,-1,1206,-1,293,1202,-2,2,283,101,1,283,283,1,68,283,283,22001,0,-3,-3,21201,-2,1,-2,1106,0,263,22101,0,-3,-3,109,-4,2106,0,0,109,4,21101,0,1,-3,21102,1,0,-2,20207,-2,67,-1,1206,-1,342,1202,-2,2,332,101,1,332,332,1,68,332,332,22002,0,-3,-3,21201,-2,1,-2,1105,1,312,22102,1,-3,-3,109,-4,2106,0,0,109,1,101,1,68,359,20101,0,0,1,101,3,68,367,20101,0,0,2,21101,376,0,0,1106,0,436,21202,1,1,0,109,-1,2105,1,0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944,549755813888,1099511627776,2199023255552,4398046511104,8796093022208,17592186044416,35184372088832,70368744177664,140737488355328,281474976710656,562949953421312,1125899906842624,109,8,21202,-6,10,-5,22207,-7,-5,-5,1205,-5,521,21102,1,0,-4,21101,0,0,-3,21102,1,51,-2,21201,-2,-1,-2,1201,-2,385,470,21002,0,1,-1,21202,-3,2,-3,22207,-7,-1,-5,1205,-5,496,21201,-3,1,-3,22102,-1,-1,-5,22201,-7,-5,-7,22207,-3,-6,-5,1205,-5,515,22102,-1,-6,-5,22201,-3,-5,-3,22201,-1,-4,-4,1205,-2,461,1106,0,547,21101,-1,0,-4,21202,-6,-1,-6,21207,-7,0,-5,1205,-5,547,22201,-7,-6,-7,21201,-4,1,-4,1106,0,529,21201,-4,0,-7,109,-8,2106,0,0,109,1,101,1,68,564,20101,0,0,0,109,-1,2106,0,0,1102,1297,1,66,1101,0,2,67,1101,0,598,68,1102,1,302,69,1101,1,0,71,1101,0,602,72,1106,0,73,0,0,0,0,8,17398,1102,43159,1,66,1102,4,1,67,1102,631,1,68,1102,1,302,69,1101,0,1,71,1102,1,639,72,1105,1,73,0,0,0,0,0,0,0,0,30,83914,1102,92459,1,66,1101,5,0,67,1101,0,668,68,1102,302,1,69,1101,1,0,71,1102,1,678,72,1106,0,73,0,0,0,0,0,0,0,0,0,0,37,33314,1102,41957,1,66,1102,1,2,67,1102,1,707,68,1101,302,0,69,1101,1,0,71,1102,1,711,72,1105,1,73,0,0,0,0,10,114159,1101,0,89393,66,1101,1,0,67,1101,740,0,68,1101,0,556,69,1102,1,1,71,1101,742,0,72,1106,0,73,1,81,44,59667,1102,28871,1,66,1102,1,1,67,1101,771,0,68,1102,1,556,69,1101,0,1,71,1102,773,1,72,1105,1,73,1,1559,32,39079,1102,1,32063,66,1102,2,1,67,1102,802,1,68,1102,302,1,69,1101,1,0,71,1101,0,806,72,1106,0,73,0,0,0,0,17,84914,1102,1559,1,66,1102,1,4,67,1102,1,835,68,1102,1,302,69,1102,1,1,71,1101,843,0,72,1106,0,73,0,0,0,0,0,0,0,0,10,76106,1101,0,54679,66,1102,1,1,67,1102,872,1,68,1102,556,1,69,1102,1,1,71,1101,0,874,72,1106,0,73,1,77489,44,19889,1101,42577,0,66,1102,1,1,67,1101,0,903,68,1101,556,0,69,1102,1,1,71,1102,1,905,72,1105,1,73,1,461,20,154653,1101,88873,0,66,1102,5,1,67,1102,1,934,68,1101,253,0,69,1102,1,1,71,1102,1,944,72,1105,1,73,0,0,0,0,0,0,0,0,0,0,3,5281,1101,33377,0,66,1101,1,0,67,1102,1,973,68,1102,556,1,69,1102,1,1,71,1101,0,975,72,1105,1,73,1,2395871,21,109966,1101,8779,0,66,1101,1,0,67,1102,1,1004,68,1101,0,556,69,1102,1,1,71,1101,1006,0,72,1106,0,73,1,1756,1,53871,1101,0,15761,66,1102,1,1,67,1101,1035,0,68,1101,556,0,69,1102,3,1,71,1101,1037,0,72,1106,0,73,1,3,43,147166,34,4677,39,277377,1101,0,17957,66,1102,1,3,67,1102,1,1070,68,1101,0,302,69,1102,1,1,71,1101,0,1076,72,1105,1,73,0,0,0,0,0,0,23,266619,1102,59369,1,66,1102,1,1,67,1102,1105,1,68,1101,556,0,69,1101,6,0,71,1101,0,1107,72,1106,0,73,1,7,20,206204,3,10562,43,220749,34,1559,2,172636,39,184918,1102,1,67763,66,1101,1,0,67,1102,1146,1,68,1102,556,1,69,1102,1,0,71,1101,1148,0,72,1105,1,73,1,1414,1102,1,8693,66,1102,1,1,67,1102,1175,1,68,1102,1,556,69,1102,1,0,71,1102,1177,1,72,1106,0,73,1,1808,1102,1,67057,66,1101,0,6,67,1101,0,1204,68,1101,302,0,69,1102,1,1,71,1102,1,1216,72,1106,0,73,0,0,0,0,0,0,0,0,0,0,0,0,38,88994,1101,97789,0,66,1101,1,0,67,1102,1245,1,68,1101,556,0,69,1101,0,0,71,1101,1247,0,72,1105,1,73,1,1630,1102,69653,1,66,1102,4,1,67,1102,1274,1,68,1102,1,302,69,1102,1,1,71,1101,1282,0,72,1106,0,73,0,0,0,0,0,0,0,0,45,335285,1102,45061,1,66,1101,0,1,67,1102,1,1311,68,1101,556,0,69,1101,10,0,71,1101,0,1313,72,1105,1,73,1,1,1,35914,20,51551,44,39778,32,117237,7,32063,17,42457,47,1297,8,8699,2,43159,39,92459,1101,0,5281,66,1102,1,2,67,1101,1360,0,68,1101,302,0,69,1101,0,1,71,1102,1,1364,72,1106,0,73,0,0,0,0,43,73583,1101,8699,0,66,1101,2,0,67,1102,1,1393,68,1102,302,1,69,1101,1,0,71,1102,1397,1,72,1105,1,73,0,0,0,0,2,129477,1101,0,73583,66,1102,3,1,67,1101,1426,0,68,1101,302,0,69,1102,1,1,71,1101,0,1432,72,1106,0,73,0,0,0,0,0,0,34,3118,1102,1,2161,66,1101,1,0,67,1102,1,1461,68,1101,0,556,69,1102,1,0,71,1102,1,1463,72,1106,0,73,1,1802,1102,51551,1,66,1101,4,0,67,1101,0,1490,68,1102,1,302,69,1102,1,1,71,1102,1,1498,72,1105,1,73,0,0,0,0,0,0,0,0,23,177746,1102,1,4969,66,1101,1,0,67,1102,1,1527,68,1102,556,1,69,1101,1,0,71,1101,0,1529,72,1105,1,73,1,18,21,54983,1102,44497,1,66,1101,2,0,67,1101,1558,0,68,1101,351,0,69,1102,1,1,71,1102,1562,1,72,1105,1,73,0,0,0,0,255,47969,1102,11251,1,66,1102,1,1,67,1102,1,1591,68,1101,0,556,69,1101,1,0,71,1102,1,1593,72,1106,0,73,1,9817,1,17957,1102,1,47981,66,1102,1,1,67,1102,1,1622,68,1101,0,556,69,1102,2,1,71,1102,1,1624,72,1105,1,73,1,10,41,208959,45,134114,1101,0,34261,66,1102,1,1,67,1102,1,1655,68,1101,556,0,69,1101,1,0,71,1101,1657,0,72,1105,1,73,1,-147,39,462295,1102,39079,1,66,1101,3,0,67,1102,1,1686,68,1101,0,302,69,1102,1,1,71,1101,0,1692,72,1106,0,73,0,0,0,0,0,0,23,444365,1101,31151,0,66,1101,1,0,67,1102,1721,1,68,1102,556,1,69,1102,3,1,71,1102,1723,1,72,1106,0,73,1,5,41,69653,41,278612,45,268228,1101,0,75083,66,1101,1,0,67,1102,1756,1,68,1101,0,556,69,1101,0,1,71,1102,1758,1,72,1105,1,73,1,125,41,139306,1101,0,54983,66,1102,1,2,67,1102,1787,1,68,1101,0,302,69,1102,1,1,71,1101,0,1791,72,1105,1,73,0,0,0,0,23,355492,1101,38053,0,66,1101,4,0,67,1101,1820,0,68,1101,253,0,69,1101,1,0,71,1102,1828,1,72,1106,0,73,0,0,0,0,0,0,0,0,38,44497,1102,16657,1,66,1101,3,0,67,1102,1857,1,68,1102,302,1,69,1101,0,1,71,1101,1863,0,72,1105,1,73,0,0,0,0,0,0,10,38053,1101,42457,0,66,1102,2,1,67,1102,1892,1,68,1101,302,0,69,1102,1,1,71,1102,1896,1,72,1106,0,73,0,0,0,0,47,2594,1101,91291,0,66,1102,1,1,67,1101,1925,0,68,1102,1,556,69,1102,1,1,71,1102,1927,1,72,1106,0,73,1,79481,7,64126,1101,82193,0,66,1101,0,1,67,1102,1,1956,68,1102,556,1,69,1102,1,2,71,1102,1958,1,72,1105,1,73,1,2,45,67057,45,201171,1102,1,65777,66,1102,1,1,67,1101,1989,0,68,1102,556,1,69,1101,1,0,71,1102,1,1991,72,1106,0,73,1,276,32,78158,1101,97453,0,66,1102,1,1,67,1102,1,2020,68,1102,556,1,69,1101,1,0,71,1102,1,2022,72,1105,1,73,1,160,45,402342,1102,19889,1,66,1102,3,1,67,1102,2051,1,68,1102,302,1,69,1101,1,0,71,1101,0,2057,72,1105,1,73,0,0,0,0,0,0,23,88873,1102,93151,1,66,1101,1,0,67,1101,0,2086,68,1102,556,1,69,1102,2,1,71,1102,2088,1,72,1106,0,73,1,11,34,6236,39,369836,1101,40759,0,66,1101,0,1,67,1102,2119,1,68,1101,556,0,69,1101,0,0,71,1101,0,2121,72,1106,0,73,1,1387,1101,0,93283,66,1101,3,0,67,1102,2148,1,68,1101,302,0,69,1102,1,1,71,1102,1,2154,72,1106,0,73,0,0,0,0,0,0,10,152212,1102,1,78977,66,1102,1,1,67,1101,2183,0,68,1101,0,556,69,1101,0,1,71,1102,1,2185,72,1105,1,73,1,-3030,20,103102,1101,0,47969,66,1101,1,0,67,1101,0,2214,68,1101,0,556,69,1101,0,6,71,1102,2216,1,72,1105,1,73,1,19153,30,41957,37,16657,37,49971,22,93283,22,186566,22,279849,1101,0,76081,66,1101,0,1,67,1101,2255,0,68,1102,1,556,69,1101,1,0,71,1101,2257,0,72,1106,0,73,1,1949,2,86318]

class IntCodeInterpreter:
    def __init__(self, prog, inp):
        self.mem = prog.copy()
        self.pc = 0
        self.inp = inp.copy()
        self.relative_base = 0
        self.out = []

    def _op_len(self, op):
        if op == 1:
            return 4
        elif op == 2:
            return 4
        elif op == 3:
            return 2
        elif op == 4:
            return 2
        elif op == 5:
            return 3
        elif op == 6:
            return 3
        elif op == 7:
            return 4
        elif op == 8:
            return 4
        elif op == 9:
            return 2
        elif op == 99:
            return 0

    def _read(self, pos, mode):
        if mode == 1:
            return pos
        idx = pos
        if mode == 0:
            pass
        elif mode == 2:
            idx = pos + self.relative_base
        else:
            raise Exception("Unknown mode: %d" % mode)
        if idx < 0:
            raise Exception("Relative position < 0")
        diff = idx - len(self.mem)
        if diff >= 0:
            self.mem.extend([0] * (diff+1))
        try:
            return self.mem[idx]
        except:
            print(idx, len(self.mem))
            raise

    def _write(self, pos, mode, value):
        idx = pos
        if mode == 0:
            pass
        elif mode == 2:
            idx = pos + self.relative_base
        else:
            raise Exception("Unknown mode: %d" % mode)
        if idx < 0:
            raise Exception("Relative position < 0")
        diff = idx - len(self.mem)
        if diff >= 0:
            self.mem.extend([0] * (diff+2))
        try:
            self.mem[idx] = value
        except:
            print(idx, len(self.mem))
            raise

    def run(self):
        param = 0
        try:
            while self.pc < len(self.mem):
                op = self.mem[self.pc] % 100
                params = self.mem[self.pc] // 100
                op_len = self._op_len(op)
                if(op == 99):
                    return 0
                else:
                    arg = [0,0,0]
                    param = [0,0,0]
                    if op_len > 1:
                        arg[0] = self.mem[self.pc+1]
                        param[0] = params % 10
                    if op_len > 2:
                        arg[1] = self.mem[self.pc+2]
                        param[1] = (params // 10) % 10
                    if op_len > 3:
                        arg[2] = self.mem[self.pc+3]
                        param[2] = (params // 100) % 10

                    if(op == 1):
                        self._write(arg[2], param[2],
                                self._read(arg[0], param[0]) + self._read(arg[1], param[1]))
                    elif(op == 2):
                        self._write(arg[2], param[2],
                                self._read(arg[0], param[0]) * self._read(arg[1], param[1]))
                    elif(op == 3):
                        if len(self.inp) > 0:
                            # print("INP: ", self.inp[0])
                            self._write(arg[0], param[0], self.inp[0])
                            self.inp = self.inp[1::]
                        else:
                            return None
                    elif(op == 4):
                        # print("OUT: ", self._read(arg[0], param[0]))
                        self.out.append(self._read(arg[0], param[0]))
                    elif(op == 5): # Jump if true
                        if self._read(arg[0], param[0]) != 0:
                            self.pc = self._read(arg[1], param[1])
                            op = 99
                    elif(op == 6): # Jump if false
                        if self._read(arg[0], param[0]) == 0:
                            self.pc = self._read(arg[1], param[1])
                            op = 99
                    elif(op == 7): # less than
                        if self._read(arg[0], param[0]) < self._read(arg[1], param[1]):
                            self._write(arg[2], param[2], 1)
                        else:
                            self._write(arg[2], param[2], 0)
                    elif(op == 8): # equals
                        if self._read(arg[0], param[0]) == self._read(arg[1], param[1]):
                            self._write(arg[2], param[2], 1)
                        else:
                            self._write(arg[2], param[2], 0)
                    elif(op == 9): # Set Relative base
                        self.relative_base = self.relative_base + self._read(arg[0], param[0])
                    else:
                        print("Unknown op. Halting! at %d" % self.pc)
                        return -1
                self.pc += self._op_len(op)
        except Exception as e:
            print("Failed at %d" % self.pc)
            raise

def left(dir):
    if dir == '^':
        return '<'
    elif dir == '<':
        return 'v'
    elif dir == 'v':
        return '>'
    elif dir == '>':
        return '^'
    else:
        raise Exception("Unknown dir: %s" % dir)
    
def right(dir):
    if dir == '^':
        return '>'
    elif dir == '<':
        return '^'
    elif dir == 'v':
        return '<'
    elif dir == '>':
        return 'v'
    else:
        raise Exception("Unknown dir: %s" % dir)

def forward(pos, dir):
    (x, y) = pos
    if dir == '^':
        return (x, y-1)
    elif dir == '<':
        return (x-1, y)
    elif dir == 'v':
        return (x, y+1)
    elif dir == '>':
        return (x+1, y)
    else:
        raise Exception("Unknown dir: %s" % dir)


for dir in ['v', '<', '>', '^']:
    if left(right(dir)) != dir:
        raise Exception("left and right doesn't match")
    if right(left(dir)) != dir:
        raise Exception("left and right doesn't match")
    if right(dir) == dir:
        raise Exception("right doesn't match")

def clear():
    print("\x1b[2J")

def goto(x, y):
    sys.stdout.write("\x1b[%d;%dH" % (y, x))

# map = [[0 for x in range(60)] for y in range(30)]

pos = (0, 0)

def find(tile):
    for y in range(len(map)):
        row = map[y]
        for x in range(len(row)):
            if row[x] == tile:
                return (x, y)
    raise Exception("Not found")

def move_to_result(dir, interp):
    interp.inp = [dir]
    interp.out = []
    while len(interp.out) == 0:
        interp.run()

def rev(dir):
    if dir == 1:
        return 2
    if dir == 2:
        return 1
    if dir == 3:
        return 4
    if dir == 4:
        return 3
    raise Exception("Unknown dir: %d" % dir)

def new_pos(dir):
    if dir == 1:
        return (pos[0], pos[1]-1)
    if dir == 2:
        return (pos[0], pos[1]+1)
    if dir == 3:
        return (pos[0]-1, pos[1])
    if dir == 4:
        return (pos[0]+1, pos[1])
    raise Exception("Unknown dir: %d" % dir)

def new_dirs(dir):
    if dir == 1:
        return [1,3,4]
    if dir == 2:
        return [2,3,4]
    if dir == 3:
        return [1,2,3]
    if dir == 4:
        return [1,2,4]
    raise Exception("Unknown dir: %d" % dir)

def search(interp, themap):
    global pos

    path=[]
    tries=dict()
    tries[pos] = (0, [1, 2, 3, 4])
    themap[pos] = '.'

    while len(tries) > 0:
        curr = tries[pos]

        if len(curr[1]) == 0:
            # Done here, backtrack
            if curr[0] == 0:
                # Done!
                return
            dir = curr[0]
            move_to_result(dir, interp)
            if interp.out[0] == 0:
                raise Exception("Confused...")
            del tries[pos]
            pos = new_pos(dir)
        else:
            dir = curr[1].pop()
            np = new_pos(dir)
            if not np in themap:
                move_to_result(dir, interp)
                if interp.out[0] == 0:
                    themap[np] = '#'
                else:
                    if interp.out[0] == 1:
                        themap[np] = '.'
                    else:
                        themap[np] = 'O'
                    tries[np] = (rev(dir), new_dirs(dir))
                    pos = np

def is_intersect(themap, p):
    if themap.get((p[0]-1, p[1]), ' ') == '#' and themap.get((p[0]+1, p[1]), ' ') == '#' and themap.get((p[0], p[1]-1), ' ') == '#' and themap.get((p[0], p[1]+1), ' ') == '#':
        return True
    return False

def is_robot(c):
    if c == '^' or c == 'v' or c == '<' or c == '>':
        return True
    return False

def get_at_most(n, s, others):
    while True:
        found = False
        for o in others:
            if s.find(o) == 0:
                s = s[len(o)::]
                found = True
        if not found:
            break
    result = s[:n+1]
    pos = result.rfind(',')
    return result[0:pos+1]

def compress(s, words):
    result = []
    while True:
        found = False
        for i, word in enumerate(words):
            if s.find(word) == 0:
                s = s[len(word)::]
                found = True
                result.append('ABCD'[i])
        if not found:
            break
    if len(s) == 0 and len(result) <= 10:
        return ",".join(result)

def find_solution(directives):
    for max_a in range(2, 21):
        a = get_at_most(max_a, directives, [])
        for max_b in range(2, 21):
            b = get_at_most(max_b, directives, [a])
            for max_c in range(2, 21):
                c = get_at_most(max_c, directives, [a, b])
                res = compress(directives, [a, b, c])
                if res and len(res) <= 21:
                    return [res, a[:-1], b[:-1], c[:-1]]

def is_x_y_affected(x, y):
    interp = IntCodeInterpreter(prog, [x, y])
    interp.run()
    if interp.out[0] == 1:
        return True
    else:
        return False

def get_min_x(y, min_x=-1):
    if min_x == -1:
        for x in range(y):
            if is_x_y_affected(x, y):
                return x
    else:
        if is_x_y_affected(min_x, y):
            for x in range(min_x)[::-1]:
                if not is_x_y_affected(x, y):
                    return x+1
        else:
            for x in range(min_x, y+1):
                if is_x_y_affected(x, y):
                    return x

def get_max_x(y, max_x=-1):
    if max_x == -1:
        for x in range(y)[::-1]:
            if is_x_y_affected(x, y):
                return x
    else:
        if is_x_y_affected(max_x, y):
            for x in range(max_x + 1, y):
                if not is_x_y_affected(x, y):
                    return x-1
        else:
            for x in range(max_x)[::-1]:
                if is_x_y_affected(x, y):
                    return x


def get_min_max(y, min_x=-1, max_x=-1):
    return (get_min_x(y, min_x), get_max_x(y, max_x))

last_nat = (-1,-1)
nat = (0,0)

nics = []
for i in range(50):
    nics.append(IntCodeInterpreter(prog, [i]))
while True:
    anyWork = False
    for i, nic in enumerate(nics):
        if len(nic.inp) == 0:
            nic.inp = [-1]
        else:
            anyWork = True
        nic.run()
        while len(nic.out) > 0:
            print("Got out")
            if nic.out[0] == -1:
                nic.out = []
            else:
                dest, x, y = nic.out[0:3]
                print("PKT: ", dest, x, y)
                nic.out=nic.out[3:]
                anyWork = True
                if dest == 255:
                    nat = (x, y)
                else:
                    nics[dest].inp.append(x)
                    nics[dest].inp.append(y)
    if not anyWork:
        # IDLE!
        if last_nat[1] == nat[1]:
            print(nat[1])
            sys.exit(0)
        nics[0].inp.append(nat[0])
        nics[0].inp.append(nat[1])
        last_nat = nat
