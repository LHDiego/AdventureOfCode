# https://adventofcode.com/2020/day/8
# 1. What value is in the accumulator?
# 2. What is the value of the accumulator after the program terminates?

data = [l.split(" ") for l in open("input.txt").read().splitlines()]

def create_machine(program):
    return {
        "mem": program,
        "pc": 0,
        "acc": 0
    }

def op_acc(machine, value):
    machine["acc"] += int(value)
    return 1

def op_jmp(machine, value):
    return value

def op_nop(machine, value):
    return 1

inst = {
    "nop": op_nop,
    "jmp": op_jmp,
    "acc": op_acc
}

def run_machine(machine):
    tmp = set({})
    while True:
        pc = machine["pc"]
        if pc in tmp:
            return False
        if pc >= len(machine["mem"]):
            return True
        tmp.add(pc)
        op = machine["mem"][pc]
        pc += inst[op[0]](machine, int(op[1]))
        machine["pc"] = pc

machine = create_machine(data)
run_machine(machine)
print("#Part 1:", machine["acc"])

for i in range(len(data)):
    instruction = data[i]
    prev = instruction[0]
    if (instruction[0]=="nop"):
        instruction[0]="jmp"
    elif instruction[0]=="jmp":
        instruction[0]="nop"

    machine = create_machine(data)
    if run_machine(machine):
        break
    instruction[0]=prev

print("#Part 2:", machine["acc"])