#!/usr/bin/env python3

import itertools
import sys

prog = [109,424,203,1,21101,11,0,0,1105,1,282,21101,18,0,0,1106,0,259,2102,1,1,221,203,1,21101,0,31,0,1106,0,282,21102,38,1,0,1105,1,259,20101,0,23,2,22101,0,1,3,21101,1,0,1,21101,0,57,0,1105,1,303,2101,0,1,222,20102,1,221,3,21001,221,0,2,21101,0,259,1,21101,80,0,0,1105,1,225,21101,137,0,2,21101,91,0,0,1105,1,303,1202,1,1,223,21001,222,0,4,21102,259,1,3,21101,225,0,2,21102,225,1,1,21101,0,118,0,1106,0,225,20102,1,222,3,21101,0,88,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1106,0,259,1202,1,1,223,20102,1,221,4,20101,0,222,3,21101,24,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,20102,1,23,1,21101,-1,0,3,21101,0,214,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2102,1,-4,249,22102,1,-3,1,22102,1,-2,2,22102,1,-1,3,21101,0,250,0,1105,1,225,22102,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,343,1,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,1,384,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22101,0,1,-4,109,-5,2106,0,0]



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

clear()

themap = dict()
count = 0
for y in range(50):
    for x in range(50):
        interp = IntCodeInterpreter(prog, [x, y])
        interp.out = []
        interp.run()
        if interp.out[0] == 1:
            themap[(x,y)] = '#'
            count = count + 1
        else:
            themap[(x,y)] = '.'

print(count)



