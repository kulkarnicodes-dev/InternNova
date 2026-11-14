# task5_modules.py
import math
import random
import datetime

# 1. math
num = 144
print("Square root of", num, "=", math.sqrt(num))
print("Factorial of 5 =", math.factorial(5))
print("Value of pi =", round(math.pi, 4))

# 2. random
print("Random number (1-100):", random.randint(1, 100))
print("Random choice:", random.choice(["Python", "Java", "C++"]))

# 3. datetime
now = datetime.datetime.now()
print("Current date & time:", now.strftime("%d-%m-%Y %H:%M:%S"))
print("Day of week:", now.strftime("%A"))
