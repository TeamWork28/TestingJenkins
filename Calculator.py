import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator(operation, num1, num2):
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)
    else:
        return "Error: Invalid operation"

# Ensure correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python3 Calculator.py <operation> <num1> <num2>")
    sys.exit(1)

# Read command-line arguments
operation = sys.argv[1].lower()
try:
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: Please provide valid numbers.")
    sys.exit(1)

# Perform calculation
result = calculator(operation, num1, num2)
print(f"Result: {result}")
