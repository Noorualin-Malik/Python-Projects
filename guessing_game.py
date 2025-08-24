import random

secret_number = random.randint(1, 10)
print("--------------Welcome to the game! You have 7 tries to guess the number from 1 to 10.---------------")

guess_count = 0
max_attempts = 7 

while guess_count < max_attempts:
    user = input(f"Attempt {guess_count + 1}/{max_attempts} - Enter your guessing number: ")
    try:
        user_input = int(user)
    except ValueError:
        print("That's not a valid number! Please try again.")
        continue  
    
    guess_count += 1  
    
    if user_input < secret_number:
        print("Too low, guess again.")
    elif user_input > secret_number:
        print("Too high, guess again.")
    else:
        print(f"You got it! The number was {secret_number}")
        print(f"It took you {guess_count} guesses.")
        break
else:
    print(f"Game over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")
