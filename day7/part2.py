#!/usr/bin/env python3

import itertools

prog1 = [ 3,15, 3,16, 1002,16,10,16, 1,16,15,15, 4,15, 99, 0, 0]
prog2 = [ 3,23,3,24,1002,24,10,24,1002,23,-1,23, 101,5,23,23,1,24,23,23,4,23,99,0,0]
prog3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
prog4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
prog = [3,8,1001,8,10,8,105,1,0,0,21,38,47,64,85,106,187,268,349,430,99999,3,9,1002,9,4,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,101,3,9,9,102,5,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,3,9,101,2,9,9,102,4,9,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]


class IntCodeInterpreter:
    def __init__(self, prog, inp):
        self.mem = prog.copy()
        self.mem.append(0)
        self.mem.append(0)
        self.pc = 0
        self.inp = inp.copy()
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
        elif op == 99:
            return 0

    def _read(self, pos, mode):
        if mode == 0:
            return self.mem[pos]
        if mode == 1:
            return pos
        else:
            raise Exception("Unknown mode: %d" % mode)

    def _write(self, pos, mode, value):
        if mode == 0:
            self.mem[pos] = value
        else:
            raise Exception("Unknown mode: %d" % mode)

    def run(self):
        param = 0
        try:
            while self.pc < len(self.mem):
                op = self.mem[self.pc] % 100
                param = self.mem[self.pc] // 100
                if(op == 99):
                    return 0
                else:
                    arg1 = self.mem[self.pc+1]
                    param1 = param % 10
                    arg2 = self.mem[self.pc+2]
                    param2 = (param // 10) % 10
                    arg3 = self.mem[self.pc+3]
                    param3 = (param // 100) % 10
                    if(op == 1):
                        self._write(arg3, param3,
                                self._read(arg1, param1) + self._read(arg2, param2))
                    elif(op == 2):
                        self._write(arg3, param3,
                                self._read(arg1, param1) * self._read(arg2, param2))
                    elif(op == 3):
                        if len(self.inp) > 0:
                            # print("INP: ", self.inp[0])
                            self._write(arg1, param1, self.inp[0])
                            self.inp = self.inp[1::]
                        else:
                            return None
                    elif(op == 4):
                        # print("OUT: ", self._read(arg1, param1))
                        self.out.append(self._read(arg1, param1))
                    elif(op == 5): # Jump if true
                        if self._read(arg1, param1) != 0:
                            self.pc = self._read(arg2, param2)
                            op = 99
                    elif(op == 6): # Jump if false
                        if self._read(arg1, param1) == 0:
                            self.pc = self._read(arg2, param2)
                            op = 99
                    elif(op == 7): # less than
                        if self._read(arg1, param1) < self._read(arg2, param2):
                            self._write(arg3, param3, 1)
                        else:
                            self._write(arg3, param3, 0)
                    elif(op == 8): # equals
                        if self._read(arg1, param1) == self._read(arg2, param2):
                            self._write(arg3, param3, 1)
                        else:
                            self._write(arg3, param3, 0)
                    else:
                        print("Unknown op. Halting! at %d" % self.pc)
                        return -1
                self.pc += self._op_len(op)
        except Exception as e:
            print("Failed at %d" % self.pc)
            raise

max_result = 0
for p in itertools.permutations([5,6,7,8,9]):
    
    amp = []
    done = []
    for phase in p:
        amp.append(IntCodeInterpreter(prog, [phase]))
        done.append(False)

    amp[0].inp.append(0)

    i = 0
    result = 0
    while True:
        n = (i + 1) % len(p)
        if amp[i].run() != None:
            done[i] = True
        if len(amp[i].out) > 0:
            if i == len(p)-1:
                result = amp[i].out[-1]
            amp[n].inp.extend(amp[i].out)
            amp[i].out.clear()
        if not False in done:
            break
        i = n

    if result > max_result:
        max_result = result
        print(p, max_result)
