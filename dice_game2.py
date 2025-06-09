# Import the random module for generating random numbers
import random

# Loops until the user choose to exit
while True:
    
    choice=input("Roll the dice? (Y/N): ").upper() # Change input to uppercase

     # If user chooses to roll the die
    if choice == "Y":
        # Generate two random numbers between 1 and 6 (inclusive)
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1},{dice2})")

        # If same number on both die (doubles)
        if dice1 == dice2:
            print("Wow! You rolled doubles!\n")
        else:
            print("Nice roll!\n")

    # If user chooses not to roll    
    elif choice == "N":
        print("Thanks for playing!")
        break # Exit the loop and end the game

    # If the input is neither Y nor N    
    else:
        print("Invalid!")  # Handles invalid input
