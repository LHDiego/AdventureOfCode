# https://adventofcode.com/2020/day/7
# 1. How many bag colors can eventually contain at least one shiny gold bag?
# 2. How many individual bags are required inside your single shiny gold bag?

data = open("input.txt").read().splitlines()

bags = {}
for line in data:
    splitted = line.split(" contain ")
    bag = " ".join(splitted[0].split(" ")[0:2])

    contain = {}
    for x in splitted[1].split(", "):
        if not x.startswith("no"):
            contain_splitted = x.split(" ")
            bag_name = " ".join(contain_splitted[1:3])
            contain[bag_name]=int(contain_splitted[0])

    bags[bag] = contain

def can_contain_bag(bags, bag_name, can_contain):
    container = bags.get(bag_name, {})
    if can_contain in container:
        return True
    
    for i in container.keys():
        if can_contain_bag(bags, i, can_contain):
            return True

    return False

total_shiny_gold_containers = 0
for bag in bags:
    if can_contain_bag(bags, bag, "shiny gold"):
        total_shiny_gold_containers += 1

print("#Part 1:", total_shiny_gold_containers)

def how_many_bags_can_contain(bags, bag_name):
    container = bags.get(bag_name, {})
    total = 0
    for bag, number in container.items():
        total += (1 + how_many_bags_can_contain(bags, bag)) * number
    return total

print("#Part 2:", how_many_bags_can_contain(bags, "shiny gold"))