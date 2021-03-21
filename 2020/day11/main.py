# https://adventofcode.com/2020/day/11
# 1. How many seats end up occupied?
# 2. Given the new visibility method and the rule change for occupied seats becoming empty, how many seats end up occupied?

data = [list(l) for l in open("input.txt").read().splitlines()]

def is_position_valid(seats, x, y):
    if x<0 or x>=len(seats[0]) or y<0 or y>=len(seats):
        return False
    return True

def get_seat(seats, x, y):
    if not is_position_valid(seats, x, y):
        return "."
    return seats[y][x]

def is_occupied(seats, x, y):
    return get_seat(seats, x, y) == "#"

def get_total_adjacent_occupied(seats, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i==0 and j==0:
                continue
            if is_occupied(seats, x+j, y+i):
                total += 1
    return total

def get_total_ray_occupied(seats, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i==0 and j==0:
                continue
            tx = x
            ty = y

            while True:
                tx += j
                ty += i
                if not is_position_valid(seats, tx, ty) or get_seat(seats, tx, ty) == "L":
                    break
                if get_seat(seats, tx, ty) == "#":
                    total += 1
                    break
    return total

def get_total_occupied_seats(seats):
    total = 0
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if is_occupied(seats, x, y):
                total += 1
    return total

def draw_seats(seats):
    for i in seats:
        print(" ".join(i))

def step(seats, occupied_change = 4, func_occupied = get_total_adjacent_occupied):
    changed = False
    new_seats = [i.copy() for i in seats]
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            seat_state = get_seat(seats, x, y)
            if seat_state != ".":
                total_occupied = func_occupied(seats, x, y)
                if seat_state == "#":
                    if total_occupied>=occupied_change:
                        new_seats[y][x] = "L"
                        changed = True
                else:
                    if total_occupied==0:
                        new_seats[y][x] = "#"
                        changed = True
    return new_seats, changed

seats_area = [i.copy() for i in data]
changed = True
while changed:
    seats_area, changed = step(seats_area)

print("#Part 1:", get_total_occupied_seats(seats_area))

seats_area = [i.copy() for i in data]
changed = True
while changed:
    seats_area, changed = step(seats_area, 5, get_total_ray_occupied)
print("#Part 2:", get_total_occupied_seats(seats_area))