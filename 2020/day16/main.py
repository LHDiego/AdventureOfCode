# https://adventofcode.com/2020/day/16
# 1. What is your ticket scanning error rate?
# 2. What do you get if you multiply those six values together?

data = open("input.txt").read().splitlines()

rules = {}
ranges = []

# Rules
while True:
    line = data.pop(0)
    if line=="": break

    splitted = line.split(": ")
    key = splitted[0]
    values = [l.split("-") for l in splitted[1].split(" or ")]
    for i in range(len(values)):
        values[i] = [int(x) for x in values[i]]

    rules[key] = values
    ranges += values

# Your ticket
data.pop(0)
your_ticket = [int(n) for n in data.pop(0).split(",")]
data.pop(0)

# Nearby ticket
data.pop(0)
nearby_tickets = []
while len(data)>0:
    nearby_tickets.append([int(n) for n in data.pop(0).split(",")])

# Find invalid ranges
valids = []
invalid = []
for ticket in nearby_tickets:
    is_ticket_valid = True
    for n in ticket:
        is_valid = False
        for ran in ranges:
            if n>=ran[0] and n<=ran[1]:
                is_valid = True
                break
        if not is_valid:
            is_ticket_valid = False
            invalid.append(n)
    if is_ticket_valid:
        valids.append(ticket)

print("#Part 1:", sum(invalid))

valids.append(your_ticket)

# Valid fields
fields = []
for i in range(len(your_ticket)):
    fields.append(list(rules.keys()))

# Check fields with every number
for ticket in valids:
    for i in range(len(ticket)):
        num = ticket[i]
        place_fields = fields[i]
        if len(place_fields)==1: continue

        remove_rule = []
        for j in range(len(place_fields)):
            field_name = place_fields[j]
            ranges = rules[field_name]

            rule_valid = (num>=ranges[0][0] and num<=ranges[0][1]) or (num>=ranges[1][0] and num<=ranges[1][1])

            if not rule_valid:
                remove_rule.append(field_name)
        for r in remove_rule:
            place_fields.remove(r)

        if len(place_fields) == 1:
            to_remove = [place_fields]
            while len(to_remove)>0:
                tmp_fields = to_remove.pop(0)
                last_one = tmp_fields[0]
                for x in fields:
                    if x != tmp_fields and last_one in x:
                        x.remove(last_one)
                        if len(x) == 1:
                            to_remove.append(x)

# Get list indexes
fields_ordered = []
for i in fields:
    fields_ordered += i
find = [i for i in fields_ordered if i.startswith("departure")]
indexes = [fields_ordered.index(i) for i in find]

p2_result = 1
for i in indexes:
    p2_result *= your_ticket[i]
print("#Part 2:", p2_result)