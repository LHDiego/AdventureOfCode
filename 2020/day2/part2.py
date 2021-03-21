# https://adventofcode.com/2020/day/2
# How many passwords are valid according to their policies?

data = open("input.txt").read().splitlines()

total_valid = 0
for line in data:
    splitted = line.split(":")
    rules = splitted[0].split(" ")
    letter_range = [int(n) for n in rules[0].split("-")]
    letter = rules[1]
    password = splitted[1][1:]

    first = password[letter_range[0]-1]==letter
    second = password[letter_range[1]-1]==letter
    if (first and not second) or (not first and second):
        total_valid += 1

print("Total valid passwords:", total_valid)