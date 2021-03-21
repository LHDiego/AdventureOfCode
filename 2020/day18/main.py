# https://adventofcode.com/2020/day/16
# 1. Evaluate the expression on each line of the homework; what is the sum of the resulting values?
# 2. What do you get if you add up the results of evaluating the homework problems using these new rules?

import re

with open("input.txt") as file:
    data = [l.replace(" ", "") for l in file.read().splitlines()]

def op_add(a, b):
    return a+b

def op_mult(a, b):
    return a*b

operations = {
    "+": op_add,
    "*": op_mult
}

def split_expression(expression):
    return [int(i) if i.isnumeric() else i for i in re.split("(\d+)", expression)[1:-1]]

def resolve(expression):
    num = expression.pop(0)
    while len(expression)>0:
        op = expression.pop(0)
        num = operations[op](num, expression.pop(0))
    return num

def resolve_advanced(expression):
    while "+" in expression:
        index = expression.index("+")
        expression.pop(index)
        num1 = expression.pop(index-1)
        num2 = expression.pop(index-1)
        expression.insert(index-1, num1+num2)

    num = expression.pop(0)
    while len(expression)>0:
        op = expression.pop(0)
        num = operations[op](num, expression.pop(0))
    return num

def evaluate(expression, resolver = resolve):
    index_start = 0
    while "(" in expression:
        index = expression.find("(", index_start)
        index2 = expression.find(")", index+1)+1
        index3 = expression.find("(", index+1)

        if index2<index3 or index3 == -1:
            part = expression[index+1:index2-1]
            op = split_expression(part)
            result = resolver(op)

            expression = expression[:index] + str(result) + expression[index2:]
            index_start = 0
        else:
            index_start = index3
    
    splitted = split_expression(expression)
    return resolver(splitted)

total = 0
for expression in data:
    total += evaluate(expression)
print("#Part 1:", total)

total = 0
for expression in data:
    total += evaluate(expression, resolver=resolve_advanced)
print("#Part 2:", total)