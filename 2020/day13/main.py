# https://adventofcode.com/2020/day/13
# 1. What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
# 2. What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?

data = open("input.txt").read().splitlines()
data[0] = int(data[0])
data[1] = [int(x) if x.isnumeric() else x for x in data[1].split(",")]

early_id = -1
early_time = 0
for bus in data[1]:
    if bus == 'x': continue
    time = bus - (data[0] % bus)
    if early_id == -1 or time < early_time:
        early_id = bus
        early_time = time 

print(f"#Part 1: Early bus ID is {early_id}, need wait {early_time} minutes. Result -> {(early_id*early_time)}")

def get_mcm(a, b):
    temp = a
    while temp % b != 0:
        temp += a
    return temp

def calculate(tmp, a, b, offset):
    while True:
        tmp += a
        if (tmp+offset) % b == 0:
            break 
    return tmp

time = 0
n1 = data[1][0]
for i in range(1, len(data[1])):
    if data[1][i] == 'x':
        continue
    n2 = data[1][i]
    time = calculate(time, n1, n2, i)
    n1 = get_mcm(n1, n2)

print("#Part 2:", time)