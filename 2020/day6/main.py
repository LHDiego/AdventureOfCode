data = open('input.txt').read().splitlines()

# split in groups
groups = []
curr = []
for i in range(len(data)):
    is_empty = data[i] == ''

    if not is_empty:
        curr.append(data[i])

    if is_empty or i==len(data)-1:
        groups.append(curr)
        curr = []

def get_different_answers(group):
    tmp = set()
    for i in group:
        tmp.update(list(i))
    return len(tmp)

total_part_1 = 0
for g in groups:
    num = get_different_answers(g)
    total_part_1 += num
    print(f'El grupo {g} tiene {num} respuestas diferentes')
print(f'Part 1 result => {total_part_1}')

def get_same_answers(group):
    tmp = {}
    for i in group:
        for j in list(i):
            tmp[j] = tmp.get(j, 0) + 1
    total = len(list(filter(lambda elem: elem[1] == len(group), tmp.items())))
    return total

total_part_2 = 0
for g in groups:
    num = get_same_answers(g)
    total_part_2 += num
    print(f'El grupo {g} tiene {num} respuestas iguales')
print(f'Part 2 result => {total_part_2}')