# https://adventofcode.com/2020/day/17
# 2. How many cubes are left in the active state after the sixth cycle?

data = open("input.txt").read().splitlines()

def create_world(data):
    world = {
        "cubes": {},
        "x1": 0,
        "x2": len(data[0])-1,
        "y1": 0,
        "y2": len(data)-1,
        "z1": 0,
        "z2": 0,
        "w1": 0,
        "w2": 0
    }

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                key = get_key(x, y, 0, 0)
                world["cubes"][key]=create_cube(x, y, 0, 0)

    return world

def get_key(x, y, z, w):
    return f"{x},{y},{z},{w}"

def create_cube(x, y, z, w):
    return [x, y, z, w]

def get_total_neighbors_active(world, x, y, z, w):
    key = get_key(x, y, z, w)
    cube = world["cubes"].get(key, create_cube(x, y, z, w))
    total_actives = 0
    for ty in range(y-1, y+2):
        for tx in range(x-1, x+2):
            for tz in range(z-1, z+2):
                for tw in range(w-1, w+2):
                    if tx==x and ty==y and tz==z and tw==w: continue
                    key_other = get_key(tx, ty, tz, tw)
                    if key_other in world["cubes"]:
                        total_actives += 1
    return total_actives

def step_world(world):
    cubes_new = {}
    for y in range(world["y1"]-1, world["y2"]+2):
        for x in range(world["x1"]-1, world["y2"]+2):
            for z in range(world["z1"]-1, world["z2"]+2):
                for w in range(world["w1"]-1, world["w2"]+2):
                    key = get_key(x, y, z, w)
                    is_active = key in world["cubes"]
                    total_neighbors_active = get_total_neighbors_active(world, x, y, z, w)
                    if is_active and (total_neighbors_active==2 or total_neighbors_active==3):
                        cubes_new[key] = world["cubes"][key]
                    elif not is_active and total_neighbors_active==3:
                        cubes_new[key] = create_cube(x, y, z, w)
    
    world["cubes"]=cubes_new
    world["x1"] -= 1
    world["x2"] += 1
    world["y1"] -= 1
    world["y2"] += 1
    world["z1"] -= 1
    world["z2"] += 1
    world["w1"] -= 1
    world["w2"] += 1

world = create_world(data)

print(len(world["cubes"]))
for i in range(6):
    print("#Step", i+1)
    step_world(world)
    print(len(world["cubes"]))

print("#Part 2:", len(world["cubes"]))