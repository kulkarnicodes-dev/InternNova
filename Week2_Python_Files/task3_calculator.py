# task3_calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Operations: +  -  *  /  %")
op = input("Choose operation: ")

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", subtract(a, b))
elif op == "*":
    print("Result:", multiply(a, b))
elif op == "/":
    print("Result:", divide(a, b))
elif op == "%":
    print("Result:", modulus(a, b))
else:
    print("Invalid operation!")
