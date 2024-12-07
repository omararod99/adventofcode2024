import re

inputs = open("day3/inputs.txt", 'r')
memory = inputs.read()

mul_matches = re.findall("mul\(\d+,\d+\)", memory)

print(mul_matches)
total = 0  

for i in range(0,len(mul_matches)):
    multiples = (re.findall("(\d+),(\d+)", mul_matches[i]))
    sum_group = 1

    print(multiples)
    for j in multiples[0]:
        sum_group *= int(j)

    total += sum_group

print(total)