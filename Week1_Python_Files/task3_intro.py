# Task 3: Input, Output and Type Casting

name = input("Enter your name: ")
age_text = input("Enter your age: ")
city = input("Enter your city: ")

print("Type of age before casting:", type(age_text))
age = int(age_text)                      # type casting str -> int
print("Type of age after casting :", type(age))

print()
print(f"Hello! My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"Next year I will be {age + 1} years old.")
