# https://adventofcode.com/2020/day/5
# What is the highest seat ID on a boarding pass?

import math

data = open('input.txt').read().splitlines()

def decoding_seat(seat):
    row_low = 0
    row_up = 127
    column_low = 0
    column_up = 7

    for i in seat[:-3]:
        change = max(math.ceil((row_up - row_low) / 2.0), 1)
        if i=='F':
            row_up -= change
        else:
            row_low += change
            

    for i in seat[-3:]:
        change = max(math.ceil((column_up - column_low) / 2.0), 1)
        if i=='L':
            column_up -= change
        else:
            column_low += change

    return [row_low, column_low]

# part 1
all_ids = []
highest = 0
for line in data:
    dec = decoding_seat(line)
    seat_id = 8*dec[0]+dec[1]
    print(f"{line}: row {dec[0]}, column {dec[1]}, seat ID {seat_id}")
    highest = max(highest, seat_id)
    all_ids.append(seat_id)
print("Highest seat ID:", highest)

# part 2
all_ids.sort()
for i in range(1, len(all_ids)):
    if all_ids[i] - all_ids[i-1] == 2:
        print("You seat ID is:", all_ids[i]-1)
        break