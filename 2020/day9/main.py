# https://adventofcode.com/2020/day/9
# 1. What is the first number that does not have this property?
# 2. What is the encryption weakness in your XMAS-encrypted list of numbers?

data = [int(n) for n in open("input.txt").read().splitlines()]

def get_invalid_numbers(numbers, preamble):
    invalid = []
    for i in range(preamble, len(numbers)):
        num = numbers[i]
        tmp = set({})
        is_valid = False
        for j in range(1, preamble+1):
            num2 = numbers[i-j]
            if (num-num2) in tmp:
                is_valid = True
                break
            tmp.add(num2)
        
        if not is_valid:
            invalid.append(num)
    return invalid

invalid_number = get_invalid_numbers(data, 25)[0]
print("#Part 1:", invalid_number)

def get_contiguous_numbers(numbers, num_find):
    total = 0
    num_list = []
    for i in range(len(numbers)):
        num = numbers[i]
        num_list.append(num)
        total += num
        while total > num_find:
            total -= num_list.pop(0)
        if total == num_find:
            break
    return num_list

contiguous_numbers = get_contiguous_numbers(data, invalid_number)
contiguous_numbers.sort()
print("#Part 2:", contiguous_numbers[0] + contiguous_numbers[-1])