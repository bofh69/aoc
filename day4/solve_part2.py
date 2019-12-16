#!/usr/bin/env python3

min = 372037
max = 905157

count = 0


for a1 in range(9-3):
    b1 = a1 + 3
    for a2 in range(10-b1):
        b2 = a2 + b1
        for a3 in range(10-b2):
            b3 = a3 + b2
            for a4 in range(10-b3):
                b4 = a4 + b3
                for a5 in range(10-b4):
                    b5 = a5 + b4
                    for a6 in range(10-b5):
                        b6 = a6 + b5
                        if a2 == 0 or a3 == 0 or a4 == 0 or a5 == 0 or a6 == 0:
                            digits = [b1, b2, b3, b4, b5, b6]
                            last = -1
                            repeat = 1
                            for d in digits:
                                if d == last:
                                    repeat += 1
                                else:
                                    if repeat == 2:
                                        break
                                    last = d
                                    repeat = 1
                            val = b1 * 100000 + b2 * 10000 + b3 * 1000 + b4 * 100 + b5 * 10 + b6
                            if val >= max:
                                break
                            if repeat == 2:
                                if val >= min:
                                    print("    %d %d %d %d %d %d" % (b1, b2, b3, b4, b5, b6))
                                    last = -1
                                    repeat = 0
                                    for d in digits:
                                        print("D:%d l:%d r:%d" % (d, last, repeat))
                                        if d == last:
                                            repeat += 1
                                        else:
                                            if repeat == 2:
                                                break
                                            last = d
                                            repeat = 0
                                    count += 1
                            else:
                                if val >= min:
                                    print("not %d %d %d %d %d %d" % (b1, b2, b3, b4, b5, b6))


print(count)
