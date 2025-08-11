import random

choices= ["Rock", "Paper", "Scissors"]
user= input("Enter Your Choice Rock, Paper or Scissors: ").lower()
computer= random.choice(choices)

print(f"Computer Chooses {computer}")

if user== computer:
    print("It's a tie")
elif(user=="rock" and computer == "scissors") or \
(user=="paper" and computer=="rock") or \
(user=="scissors" and computer=="paper"):
    print("You win")
else:
    print("You loose")