n = 5

for i in range(n + 1):
    for j in range(i, n):
        print(" ", end=" ")
    for x in range(i):
        print("*", end= " ")
    for j in range(i + 1):
        print("*", end=" ")    
    print()    