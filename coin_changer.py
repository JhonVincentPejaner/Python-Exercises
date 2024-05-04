coins = [1000, 500,200, 100, 50, 20, 10, 5, 1]
amount = int(input("Amount: "))

change = []

for coin in coins:
    while amount >= coin:
        amount -= coin
        change.append(coin)
        
if amount <= 0:
    print(change) 