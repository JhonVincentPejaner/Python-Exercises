val = [6, 10, 8, 3, 4]
target = 12
total = 0
for i in range(1, len(val)):
    for j in range(1, len(val)):
        total = val[i] + val[j]
        
        if total == target:
            print(i)
    