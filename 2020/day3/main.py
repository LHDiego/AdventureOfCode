# https://adventofcode.com/2020/day/3
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

data = open("input.txt").read().splitlines()

def get_total_trees_encounter(map, mx, my):
    x = 0
    y = 0
    total_trees = 0

    while y<len(data):
        if data[y][x] == "#":
            total_trees += 1

        x = (x + mx) % len(data[y])
        y += my
    return total_trees

print("Total trees:", get_total_trees_encounter(data, 3, 1))

print("== Part 2 ==")
slopes = (
    get_total_trees_encounter(map, 1, 1) *
    get_total_trees_encounter(map, 3, 1) *
    get_total_trees_encounter(map, 5, 1) *
    get_total_trees_encounter(map, 7, 1) *
    get_total_trees_encounter(map, 1, 2)
)

print("Total multiply slopes:", slopes)