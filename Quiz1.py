#A simple quiz game with 3 general questions.

print("Welcome to the Quiz!")

score = 0 # Initial score is set to 0.

# Questions begin 
print("Q1: What is the capital of france?")
ans=input(" ")

if ans == "Paris":
    print("Correct!")
    score += 1 
else:
    print("Wrong!")

print("Q2: What is the sum of 3 and 7?")
ans=input(" ")

if ans == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Q3: What is the color of the sky on a clear day?")
ans=input(" ")

if ans == "Blue":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Displays final score 
print("Final Score = ", score)
