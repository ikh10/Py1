#Defined a function for calc
def basic_calculator():
    print("=== Basic Calculator === \n")

    # Loop until the user enters valid input and the calc is done
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose an operation (+, -, *, /): ")
            
            # Perform the op based on user input
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                # Check for div by zero
                if num2 == 0:
                    print("Error: Division by zero is not allowed. \n")
                    continue  # Ask again
                result = num1 / num2
            else:
                print("Invalid operation. Please enter +, -, *, or /. \n")
                continue  # Ask again

            print(f"Result: {result}")
            break  # Exit loop after successful calculation

        except ValueError:
            print("Invalid input. Please enter numeric values. \n")

# Run the calculator
basic_calculator()
