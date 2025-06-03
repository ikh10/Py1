# A more polished age category checker
# Defined a function to check age category
def age_category_checker():
    print("=== Age Category Checker === \n")
    try:
        age = int(input("Enter your age: "))
        
        # Check for negative age
        if age < 0:
            print("Invalid age! Age cannot be negative.")
        elif age <= 12:
            print("Hey Kiddo! You're still a child.")
        elif age <= 19:
            print("Teenagers ah... Enjoy your youth!")
        elif age <= 64:
            print("Adult. Welcome to the real world.")
        elif age <= 120:
            print("Senior. Hope you're enjoying life!")
        else:
            print("Can you share your secret to immortality?")
            
    # Handle non-integer input  
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Run the age checker
age_category_checker()
