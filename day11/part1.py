#!/usr/bin/env python3

import itertools

prog = [3,8,1005,8,309,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,29,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,51,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,72,1,1104,8,10,2,1105,15,10,2,1106,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,107,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,128,2,6,8,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,155,1006,0,96,2,108,10,10,1,101,4,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,188,2,1,5,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,214,2,6,18,10,1006,0,78,1,105,1,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,247,2,103,8,10,2,1002,10,10,2,106,17,10,1,1006,15,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,285,1,1101,18,10,101,1,9,9,1007,9,992,10,1005,10,15,99,109,631,104,0,104,1,21102,387507921664,1,1,21102,1,326,0,1106,0,430,21102,932826591260,1,1,21102,337,1,0,1106,0,430,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,206400850983,0,1,21101,0,384,0,1105,1,430,21102,3224464603,1,1,21102,395,1,0,1106,0,430,3,10,104,0,104,0,3,10,104,0,104,0,21102,838433657700,1,1,21102,418,1,0,1106,0,430,21101,825012007272,0,1,21101,429,0,0,1106,0,430,99,109,2,21202,-1,1,1,21101,40,0,2,21101,461,0,3,21102,1,451,0,1105,1,494,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,456,457,472,4,0,1001,456,1,456,108,4,456,10,1006,10,488,1102,1,0,456,109,-2,2106,0,0,0,109,4,1202,-1,1,493,1207,-3,0,10,1006,10,511,21101,0,0,-3,21202,-3,1,1,21201,-2,0,2,21102,1,1,3,21102,1,530,0,1106,0,535,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,558,2207,-4,-2,10,1006,10,558,22101,0,-4,-4,1106,0,626,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,577,0,1106,0,535,22102,1,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,596,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,618,21201,-1,0,1,21102,618,1,0,105,1,493,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

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

width = 10
height = 10
dir = '^'
paint = dict()
pos = (0,0)
count = 0

interp = IntCodeInterpreter(prog, [0])
while True:
    result = interp.run()
    while len(interp.out) >= 2:
        color = interp.out[0]
        move = interp.out[1]
        interp.out = interp.out[2::]
        if move == 0:
            dir = left(dir)
        elif move == 1:
            dir = right(dir)
        else:
            raise Exception("Unknown dir: %d" % move)
        paint[pos] = color
        pos = forward(pos, dir)
        if not pos in paint:
            count = count + 1
        color = paint.setdefault(pos, 0)
        interp.inp.append(color)
    if result != None:
        break

print(paint)
print(count)
