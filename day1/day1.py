inputs = open("day1/inputs.txt", 'r')
rows = inputs.read().splitlines()

split_rows = []
left_col = []
right_col = []

part1 = []
part2 = []

# part 1
for a in rows:
    split_rows.append(a.split('   '))

for b in split_rows:
    left_col.append(int(b[0]))
    right_col.append(int(b[1]))

# part 2
for j in range(0,len(left_col)):
    part2.append(left_col[j] * right_col.count(left_col[j]))

# part 1    
left_col.sort()
right_col.sort()

for k in range(0,len(right_col)):
    part1.append(abs(right_col[k] - left_col[k]))


# final numbers
print(sum(part1))
print(sum(part2))