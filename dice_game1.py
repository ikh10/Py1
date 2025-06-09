# Import the random module for generating random numbers
import random

# Ask user if they want to play the game
qts=input("Roll the dice? (Y/N): ")

if qts == "Y":
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"({dice1},{dice2})")
  
elif qts == "N":
    print("Thanks for playing!")

# Any other choice than Y or N  
else:
    print("Invalid!")
