import random



enemy = random.choice(["Rock", "Scissor", "Paper"])
print(enemy)
player = input("Rock/Paper/Scissor: ")

if player == enemy:
    print("Tie")
elif (player == "Rock" and enemy == "Scissor") or \
    (player == "Paper" and enemy == "Rock") or \
    (player == "Scissor" and enemy == "Paper"):
    print("You win")  
              
else:
    print("You lose")    
    