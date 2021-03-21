# https://adventofcode.com/2020/day/10
# 1. What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
# 2. What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

data = [int(n) for n in open("input.txt").read().splitlines()]
data.sort()

def get_jolt_differences(adapters):
    diff = {}
    prev = 0
    for a in adapters:
        num = a - prev
        diff[num] = diff.get(num, 0) + 1
        prev = a

    diff[3] = diff.get(3, 0) + 1
    return diff

jolt_differences = get_jolt_differences(data)
print("#Part 1:", jolt_differences.get(1, 0)*jolt_differences.get(3, 0))

def get_total_different_ways(adapters, index = -1, mem = {}):
    if index in mem:
        return mem[index]
    if index == len(adapters)-1:
        return 1

    total = 0
    prev = 0 if index==-1 else adapters[index] 
    for i in range(index+1, min(index+4, len(adapters))):
        diff = adapters[i] - prev
        if diff>3: break
        tmp = get_total_different_ways(adapters, i, mem)
        total += tmp
        mem[i] = tmp

    return total

print("#Part 2:", get_total_different_ways(data))