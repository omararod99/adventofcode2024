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
    for i in range(0,len(x)):
        x_changed = x.copy()
        x_changed.pop(i)
        
        if report_safe(x_changed):
            x = x_changed.copy()
            break
        else:
            x_changed = x.copy()

    return report_safe(x)

    
# count safe rows
for n in rows_div:
    print("Report: " + str(n))
    if report_safe(n):
        safe_report_count.append(True)
        print("Safe")
    else:
        if damper(n):
            safe_report_count.append(True)
            print("Changes: " + str(n))
            print("Safe")
        else:
            print("Unsafe")

print(sum(safe_report_count))