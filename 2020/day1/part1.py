# https://adventofcode.com/2020/day/1
# the two entries that sum to 2020; what do you get if you multiply them together?

data = [int(l) for l in open("./input.txt").read().splitlines()]

nums = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if (data[i]+data[j] == 2020):
            nums.append(data[i])
            nums.append(data[j]) 
    if len(nums)>0:
        break

print(nums[0] * nums[1])