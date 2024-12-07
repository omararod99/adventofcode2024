import re

inputs = open("day3/inputs.txt", 'r')
memory = inputs.read()

mul_matches = re.split("(?=don't\(\))|(?=do\(\))", memory)

do_mul = ''
reg_mul = ''
total = 0  


# combine first muls with "do" instructions
for x in mul_matches:
    if x.startswith("do()"):
        do_mul += (x)
    elif not x.startswith(("don't()", "do()")):
        reg_mul += (x)

all_mul = do_mul + reg_mul


# get all muls and calculate
mul_matches = re.findall("mul\(\d+,\d+\)", all_mul)

for i in range(0,len(mul_matches)):
    multiples = (re.findall("(\d+),(\d+)", mul_matches[i]))
    sum_group = 1

    print(multiples)
    for j in multiples[0]:
        sum_group *= int(j)

    total += sum_group

print(total)