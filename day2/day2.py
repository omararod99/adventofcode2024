inputs = open("day2/inputs.txt", 'r')
rows = inputs.read().splitlines()
rows_div = []
safe_report_count = []

for i in rows:
    rows_div.append(i.split(' '))

# convert to ints
for l in range(0,len(rows_div)):
    for m in range(0,len(rows_div[l])):
        rows_div[l][m] = int(rows_div[l][m])

# condition functions
def strict_inc(x):
    return all(i < j for i, j in zip(x, x[1:]))

def strict_dec(x):
    return all(i > j for i, j in zip(x, x[1:]))

def strict_monotonic(x):
    return strict_inc(x) or strict_dec(x)

def adjacent(x):
    return all(1 <= abs(i - j) <=3 for i, j in zip(x, x[1:]))

def report_safe(x):
    return strict_monotonic(x) and adjacent(x)

def damper(x):        
    total_neg = 0
    total_pos = 0
    differences = []
    # print(x)

    # run patcher

    # find if increment or decrement 
    for l,m in zip(range(0,len(x)),range(1,len(x))):
        if x[m]-x[l] < 0:
            total_neg += 1
        if x[m]-x[l] > 0:
            total_pos += 1
        
        differences.append(x[m]-x[l])   
    print("Differences: " + str(differences))

    if total_neg > total_pos:
        matches = [x for x in range(0,len(differences)) if differences[x] > -1 or differences[x] < -3]
        # print(matches)
        if matches[0]+1 == len(differences):
            x.pop(matches[0]+1)
        else:
            x.pop(matches[0])

    if total_pos > total_neg:
        matches = [x for x in range(0,len(differences)) if differences[x] > 3 or differences[x] < 1]
        print(matches)
        if matches[0]+1 == len(differences):
            x.pop(matches[0]+1)
        elif differences[matches[0]] > 3 and differences[matches[0]+1] < 1:
            x.pop(matches[1])
        else:
            x.pop(matches[0])

    # print(x)

    return report_safe(x)

    
# add safe rows
for n in rows_div:
    print("Original report: " + str(n))
    if report_safe(n):
        safe_report_count.append(True)
        print("Safe")
    else:
        if damper(n):
            safe_report_count.append(True)
            print("Changes: " + str(n))
            print("Safe")
        else:
            # print(n)
            print("unsafe")
    


print(sum(safe_report_count))