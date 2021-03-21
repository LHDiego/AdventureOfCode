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

    letter_counter = {}
    for l in password:
        letter_counter[l] = letter_counter.get(l, 0) + 1

    repeats = letter_counter.get(letter, 0)
    if repeats>=letter_range[0] and repeats<=letter_range[1]:
        total_valid += 1

print("Total valid passwords:", total_valid)