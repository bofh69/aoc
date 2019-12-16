#!/usr/bin/env python3

import itertools

prog1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
prog2 = [1102,34915192,34915192,7,4,7,99,0]
prog3 = [104,1125899906842624,99]
prog = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,3,0,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,34,0,1013,1101,20,0,1012,1101,536,0,1023,1101,0,23,1006,1102,1,543,1022,1102,1,27,1003,1102,25,1,1014,1102,1,29,1009,1101,0,686,1025,1101,0,30,1004,1102,1,28,1017,1102,1,35,1016,1101,765,0,1028,1102,1,33,1002,1102,1,26,1000,1102,1,822,1027,1102,1,21,1001,1102,1,1,1021,1101,31,0,1007,1101,0,39,1010,1102,36,1,1019,1101,0,32,1015,1101,0,38,1018,1101,0,24,1005,1101,22,0,1011,1101,756,0,1029,1102,1,0,1020,1102,829,1,1026,1102,1,37,1008,1101,0,695,1024,109,19,1205,2,195,4,187,1105,1,199,1001,64,1,64,1002,64,2,64,109,7,1205,-6,215,1001,64,1,64,1105,1,217,4,205,1002,64,2,64,109,-16,21108,40,42,5,1005,1015,233,1106,0,239,4,223,1001,64,1,64,1002,64,2,64,109,-13,2102,1,5,63,1008,63,33,63,1005,63,261,4,245,1105,1,265,1001,64,1,64,1002,64,2,64,109,29,21101,41,0,-9,1008,1017,41,63,1005,63,291,4,271,1001,64,1,64,1105,1,291,1002,64,2,64,109,-22,2107,27,-4,63,1005,63,307,1105,1,313,4,297,1001,64,1,64,1002,64,2,64,109,7,1207,-4,30,63,1005,63,333,1001,64,1,64,1106,0,335,4,319,1002,64,2,64,109,1,21108,42,42,6,1005,1018,353,4,341,1105,1,357,1001,64,1,64,1002,64,2,64,109,14,21101,43,0,-7,1008,1019,41,63,1005,63,377,1106,0,383,4,363,1001,64,1,64,1002,64,2,64,109,-8,21102,44,1,-1,1008,1017,47,63,1005,63,407,1001,64,1,64,1105,1,409,4,389,1002,64,2,64,109,-15,2101,0,2,63,1008,63,25,63,1005,63,433,1001,64,1,64,1105,1,435,4,415,1002,64,2,64,109,7,1201,-8,0,63,1008,63,30,63,1005,63,455,1105,1,461,4,441,1001,64,1,64,1002,64,2,64,109,-12,2108,37,10,63,1005,63,483,4,467,1001,64,1,64,1106,0,483,1002,64,2,64,109,13,21107,45,44,0,1005,1011,499,1105,1,505,4,489,1001,64,1,64,1002,64,2,64,109,-2,2107,20,-8,63,1005,63,523,4,511,1106,0,527,1001,64,1,64,1002,64,2,64,109,20,2105,1,-6,1001,64,1,64,1105,1,545,4,533,1002,64,2,64,109,-28,2102,1,1,63,1008,63,30,63,1005,63,565,1105,1,571,4,551,1001,64,1,64,1002,64,2,64,109,20,1206,0,583,1105,1,589,4,577,1001,64,1,64,1002,64,2,64,109,-7,1206,6,603,4,595,1106,0,607,1001,64,1,64,1002,64,2,64,109,-14,2101,0,2,63,1008,63,33,63,1005,63,629,4,613,1105,1,633,1001,64,1,64,1002,64,2,64,109,-4,1208,8,30,63,1005,63,655,4,639,1001,64,1,64,1105,1,655,1002,64,2,64,109,23,21107,46,47,0,1005,1019,673,4,661,1105,1,677,1001,64,1,64,1002,64,2,64,109,-2,2105,1,7,4,683,1001,64,1,64,1106,0,695,1002,64,2,64,109,3,21102,47,1,-7,1008,1013,47,63,1005,63,717,4,701,1105,1,721,1001,64,1,64,1002,64,2,64,109,-11,1202,-7,1,63,1008,63,32,63,1005,63,745,1001,64,1,64,1105,1,747,4,727,1002,64,2,64,109,10,2106,0,9,4,753,1001,64,1,64,1105,1,765,1002,64,2,64,109,-24,1207,8,28,63,1005,63,783,4,771,1106,0,787,1001,64,1,64,1002,64,2,64,109,5,1201,0,0,63,1008,63,26,63,1005,63,813,4,793,1001,64,1,64,1105,1,813,1002,64,2,64,109,28,2106,0,-1,1001,64,1,64,1105,1,831,4,819,1002,64,2,64,109,-22,1202,-1,1,63,1008,63,24,63,1005,63,857,4,837,1001,64,1,64,1106,0,857,1002,64,2,64,109,-9,2108,30,6,63,1005,63,873,1106,0,879,4,863,1001,64,1,64,1002,64,2,64,109,-2,1208,10,26,63,1005,63,899,1001,64,1,64,1106,0,901,4,885,4,64,99,21102,1,27,1,21101,0,915,0,1105,1,922,21201,1,25948,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,22101,0,1,-1,21201,-2,-3,1,21102,957,1,0,1105,1,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2106,0,0]


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
        if diff > 0:
            self.mem.extend([0] * (diff+2))
        return self.mem[idx]

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

interp = IntCodeInterpreter(prog, [2])
interp.run()
print(interp.out)
