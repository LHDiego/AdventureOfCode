# https://adventofcode.com/2020/day/12
# 1. What is the Manhattan distance between that location and the ship's starting position?
# 2. What is the Manhattan distance between that location and the ship's starting position?

data = [[l[0], int(l[1:])] for l in open("input.txt").read().splitlines()]

def create_ship():
    return {
        "x": 0,
        "y": 0,
        "wx": 10,
        "wy": 1,
        "dir": 0
    }

def move_north(ship, value):
    ship['y'] += value

def move_south(ship, value):
    ship['y'] -= value

def move_east(ship, value):
    ship['x'] += value

def move_west(ship, value):
    ship['x'] -= value

def turn_left(ship, value):
    ship['dir'] = (ship['dir'] + value + 360) % 360

def turn_right(ship, value):
    ship['dir'] = (ship['dir'] - value + 360) % 360

def move_forward(ship, value):
    d = ship['dir']
    if d == 0:
        move_east(ship, value)
    elif d == 180:
        move_west(ship, value)
    elif d == 90:
        move_north(ship, value)
    else:
        move_south(ship, value)

navigation = {
    "N": move_north,
    "S": move_south,
    "E": move_east,
    "W": move_west,
    "L": turn_left,
    "R": turn_right,
    "F": move_forward
}

ship = create_ship()
for inst in data:
    navigation[inst[0]](ship, inst[1])

distance = abs(ship['x']) + abs(ship['y'])
print(f"#Part 1: {distance}")

# part 2

def waypoint_move_north(ship, value):
    ship['wy'] += value

def waypoint_move_south(ship, value):
    ship['wy'] -= value

def waypoint_move_east(ship, value):
    ship['wx'] += value

def waypoint_move_west(ship, value):
    ship['wx'] -= value

def waypoint_turn_left(ship, value):
    wx = ship['wx']
    wy = ship['wy']
    while value >= 180:
        value -= 180
        wx = -wx
        wy = -wy
        ship['wx'] = wx
        ship['wy'] = wy
    if value > 0:
        ship['wx'] = -wy
        ship['wy'] = wx

def waypoint_turn_right(ship, value):
    wx = ship['wx']
    wy = ship['wy']
    while value >= 180:
        value -= 180
        wx = -wx
        wy = -wy
        ship['wx'] = wx
        ship['wy'] = wy
    if value > 0:
        ship['wx'] = wy
        ship['wy'] = -wx

def waypoint_move_forward(ship, value):
    ship['x'] += ship['wx'] * value
    ship['y'] += ship['wy'] * value

navigation_waypoint = {
    "N": waypoint_move_north,
    "S": waypoint_move_south,
    "E": waypoint_move_east,
    "W": waypoint_move_west,
    "L": waypoint_turn_left,
    "R": waypoint_turn_right,
    "F": waypoint_move_forward
}

ship = create_ship()
for inst in data:
    navigation_waypoint[inst[0]](ship, inst[1])

distance = abs(ship['x']) + abs(ship['y'])
print(f"#Part 2: {distance}")