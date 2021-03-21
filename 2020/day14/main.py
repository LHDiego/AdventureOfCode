# https://adventofcode.com/2020/day/14
# 1. What is the sum of all values left in memory after it completes?
# 2. What is the sum of all values left in memory after it completes?
import re

data = [l.split(" = ") for l in open("input.txt").read().splitlines()]

mem = {}
mask0 = 0
mask1 = 0
for action, value in data:
    if action == "mask":
        mask0 = int(value.replace("X", "1"), 2)
        mask1 = int(value.replace("X", "0"), 2)
    else:
        address = int(re.search("\d+", action).group(0))
        mem[address] = (int(value) & mask0) | mask1

print("#Part 1:", sum(mem.values()))

mem = {}
maskX = 0
mask1 = 0
masks = []
for action, value in data:
    if action == "mask":
        # mascaras de ayuda
        maskX = int(value.replace("0", "1").replace("X", "0"), 2)
        mask1 = int(value.replace("X", "0"), 2)

        mask = value.replace("1", "0")
        total_x = sum(1 for x in list(mask) if x == "X")

        # generar todas las combinaciones
        tmp = [0] * total_x
        combinations = []
        combinations.append(tmp.copy())
        index = 0
        while index < total_x:
            if tmp[index] == 0:
                tmp[index] = 1
                for j in range(index):
                    tmp[j] = 0
                combinations.append(tmp.copy())
                index = -1
            index += 1
        
        masks = []
        for com in combinations:
            m = mask
            for num in com:
                m = m.replace("X", str(num), 1)
            masks.append(int(m, 2))
    else:
        address = int(re.search("\d+", action).group(0))
        address = (address & maskX) | mask1

        for m in masks:
            mem[(address | m)] = int(value)

print("#Part 2:", sum(mem.values()))