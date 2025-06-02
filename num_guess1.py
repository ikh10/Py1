# Very basic number Guessing Game
# This project lets the user guess a number until they get it right
# Note: High/low feedback is not implemented in this basic version.

number = 7 # A random number is chosen
guess = -1 # Initialization with a dummy value

print("Welcome to the number guessing game!")
print("Guess the number.")

#Repeats until user gets the random number value right
while guess!= number:
    guess = int(input("Guess: ")) #Input taken from user and coverted to int

    if guess != number:
        print("Try again!")

    else:
        print("Win! ^.^")
