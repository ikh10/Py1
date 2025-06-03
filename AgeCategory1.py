#Very basic, fun age category checker
print("Age Category Checker: \n")

# Ask the user to enter their age
age=int(input("Enter your age: "))

# Determine the age category
if age<0:
    print("Invalid Age!")
elif age <= 12:
    print("Hey Kiddo! You're still a child.")
elif age <= 17:
    print("Teenagers ah... Enjoy your youth!")
elif age <=63:
    print("Adult. Welcome to the real world.")
elif age <= 160:
    print("Senior. Hope you're enjoying life!")
else:
    print("Can you share your secret to immortality?")
