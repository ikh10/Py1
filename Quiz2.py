#This version includes case-insensitive answer checking and cleaner formatting using newline characters. 

print("Welcome to the Quiz! \n")

score = 0 # Initial score is set to 0.

# Questions begin 
Q1 = input("Question 1: What is the capital of France? \n")
if Q1.lower() == "paris": # For case-insensitive cases
    print("Correct! \n") # Uses \n for formatting enhancement
    score += 1
else:
    print("Wrong! \n")

Q2 = input("Question 2: What is 3 + 7? \n")
if Q2 == "10":
    print("Correct! \n")
    score += 1
else:
    print("Wrong! \n")

Q3 = input("Question 3: What color is the sky on a clear day? \n")
if Q3.lower() == "blue":
    print("Correct! \n")
    score += 1
else:
    print("Wrong! \n")
    
# Displays final score 
print(f"Final Score = {score}/3")
