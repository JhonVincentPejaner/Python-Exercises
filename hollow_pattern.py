
height = 8

for i in range(1, height + 1):
    if i == 1 or i == 8:
        print("*" * i)
    else:
        print("*"+ " " * (i - 2) + "*")    
