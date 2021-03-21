# https://adventofcode.com/2020/day/4
# In your batch file, how many passports are valid?
import re

data = open("input.txt").read().splitlines()

text_passports = []
pp = []
for line in data:
    if line == "":
        text_passports.append(" ".join(pp))
        pp = []
        continue
    pp.append(line)
text_passports.append(" ".join(pp))

passports = []
for p in text_passports:
    map_passport = {}
    for field in p.split(" "):
        vk = field.split(":")
        map_passport[vk[0]] = vk[1]
    passports.append(map_passport)


# part 1
print("== Part 1 ==")
def is_passport_valid(passport, req_fields):
    for field in req_fields:
        if field not in passport:
            return False
    return True

total_valid = 0
req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for i in range(len(passports)):
    is_valid = is_passport_valid(passports[i], req_fields)
    total_valid += 1 if is_valid else 0
    print(f"Passport #{i+1}: {'valid' if is_valid else 'invalid'}")

print("Total valid passports:", total_valid)

# part 2
print("== Part 2 ==")
def is_passport_valid_part2(passport, req_fields):
    for field in req_fields:
        if field not in passport:
            return False

    try:
        byr = int(passport['byr'])
        if byr<1920 or byr>2002: raise Exception('BYR is invalid')

        iyr = int(passport['iyr'])
        if iyr<2010 or iyr>2020: raise Exception('IYR is invalid')

        eyr = int(passport['eyr'])
        if eyr<2020 or eyr>2030: raise Exception('EYR is invalid')
        
        hgt = passport['hgt']
        hgt_value = int(hgt[:-2])
        hgt_type = hgt[-2:]
        if hgt_type == 'cm':
            if hgt_value<150 or hgt_value>193: raise Exception('HGT is invalid')
        elif hgt_type == 'in':
            if hgt_value<59 or hgt_value>76: raise Exception('HGT is invalid')
        else:
            raise Exception('HGT is invalid')

        # hcl
        hcl = passport['hcl']
        if not re.match("^#[0-9a-f]{6}", hcl): raise Exception('HCL is invalid')

        ecl = passport['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            raise Exception('ECL is invalid')

        pid = passport['pid']
        if not re.match("^[0-9]{9}$", pid): raise Exception(f'PID is invalid: {pid}')

        return True
    except Exception as e:
        print(e)
        return False

total_valid = 0
for i in range(len(passports)):
    is_valid = is_passport_valid_part2(passports[i], req_fields)
    total_valid += 1 if is_valid else 0
    print(f"Passport #{i+1}: {'valid' if is_valid else 'invalid'}")

print("Total valid passports:", total_valid)