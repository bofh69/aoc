#!/usr/bin/env python3

import itertools

prog1 = [ 3,15, 3,16, 1002,16,10,16, 1,16,15,15, 4,15, 99, 0, 0]
prog2 = [ 3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]
prog3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
prog = [3,8,1001,8,10,8,105,1,0,0,21,38,47,64,85,106,187,268,349,430,99999,3,9,1002,9,4,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,101,3,9,9,102,5,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,3,9,101,2,9,9,102,4,9,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]

mem = []
inp = []
out = []

def op_len(op):
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

def read(pos, mode):
    if mode == 0:
        return mem[pos]
    if mode == 1:
        return pos
    else:
        raise Exception("Unknown mode: %d" % mode)

def write(pos, mode, value):
    if mode == 0:
        mem[pos] = value
    else:
        raise Exception("Unknown mode: %d" % mode)

def runit():
    global inp
    mem.append(0)
    mem.append(0)
    pc = 0
    param = 0
    try:
        while pc < len(mem):
            op = mem[pc] % 100
            param = mem[pc] // 100
            if(op == 99):
                return mem[0]
            else:
                arg1 = mem[pc+1]
                param1 = param % 10
                arg2 = mem[pc+2]
                param2 = (param // 10) % 10
                arg3 = mem[pc+3]
                param3 = (param // 100) % 10
                if(op == 1):
                    write(arg3, param3,
                            read(arg1, param1) + read(arg2, param2))
                elif(op == 2):
                    write(arg3, param3,
                            read(arg1, param1) * read(arg2, param2))
                elif(op == 3):
                    write(arg1, param1, inp[0])
                    inp = inp[1::]
                elif(op == 4):
                    out.append(read(arg1, param1))
                elif(op == 5): # Jump if true
                    if read(arg1, param1) != 0:
                        pc = read(arg2, param2)
                        op = 99
                elif(op == 6): # Jump if false
                    if read(arg1, param1) == 0:
                        pc = read(arg2, param2)
                        op = 99
                elif(op == 7): # less than
                    if read(arg1, param1) < read(arg2, param2):
                        write(arg3, param3, 1)
                    else:
                        write(arg3, param3, 0)
                elif(op == 8): # equals
                    if read(arg1, param1) == read(arg2, param2):
                        write(arg3, param3, 1)
                    else:
                        write(arg3, param3, 0)
                else:
                    print("Unknown op. Halting! at %d" % pc)
                    return -1
            pc += op_len(op)
    except Exception as e:
        print("Failed at %d" % pc)
        raise

max_result = 0
for p in itertools.permutations(range(5)):
    mem = prog.copy()
    inp = [p[0], 0]
    out.clear()

    runit()

    for amp in range(4):
        mem = prog.copy()
        inp = [p[amp+1], out[0]]
        out.clear()
        runit()

    if out[0] > max_result:
        max_result = out[0]
        print(p, max_result)
