# Task 4: Calculator using operators

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

print("\n----- Results -----")
print(f"Addition       : {num1} + {num2} = {num1 + num2}")
print(f"Subtraction    : {num1} - {num2} = {num1 - num2}")
print(f"Multiplication : {num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"Division       : {num1} / {num2} = {num1 / num2}")
    print(f"Modulus        : {num1} % {num2} = {num1 % num2}")
else:
    print("Division       : Not possible (divide by zero)")
    print("Modulus        : Not possible (divide by zero)")

print(f"Exponent       : {num1} ** {num2} = {num1 ** num2}")
