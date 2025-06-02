# This project gives hint to user whenever their value is too low or too high as compared to the correct value.
# It uses a random number insted of a pre-defined number.

import random # Imports random module

#Randomly generates a number between 1 to 100.
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 to 100.")

# Keeps looping until the user guesses the correct number
while True: # Infinite loop until the correct number is guessed
  guess = int(input("Enter your guess: "))  # Input is taken from the user

  if guess < number:
      print("Too low! Try again.")
  elif guess > number:
        print("Too high! Try again.")
  else:
      print("Congratulations! You guessed it right.")
      break  # Exits the loop when the guess is correct
