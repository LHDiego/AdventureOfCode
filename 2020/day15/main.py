# https://adventofcode.com/2020/day/15
# 1. What will be the 2020th number spoken?
# 2. What will be the 30000000th number spoken?

data = [int(n) for n in open("input.txt").readline().split(",")]

def play(game, num):
    n = game["mem"].get(num, [])
    n.append(game["turn"])
    if len(n)>2:
        n.pop(0)
    game["mem"][num] = n
    game["turn"] += 1

game = {
    "mem": {},
    "turn": 1
}

for i in data:
    play(game, i)
last_num = data[-1]

for i in range(2020 - len(data)):
    num = 0
    mem = game["mem"]
    if len(mem.get(last_num, []))==2:
        tmp = mem[last_num]
        num = tmp[-1] - tmp[0]

    play(game, num)
    last_num = num

print("#Part 1:", last_num)

game = {
    "mem": {},
    "turn": 1
}

for i in data:
    play(game, i)
last_num = data[-1]

for i in range(30000000 - len(data)):
    num = 0
    mem = game["mem"]
    if len(mem.get(last_num, []))==2:
        tmp = mem[last_num]
        num = tmp[-1] - tmp[0]

    play(game, num)
    last_num = num

print("#Part 2:", last_num)