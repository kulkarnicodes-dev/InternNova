# task2_tuples.py - Tuples in Python

# 1. Creating a tuple
colors = ("red", "green", "blue", "yellow", "green")
single = (10,)
print("Tuple:", colors)
print("Single-element tuple:", single)

# 2. Accessing elements using indexing
print("First element:", colors[0])
print("Last element:", colors[-1])

# 3. Tuple slicing
print("colors[1:4]:", colors[1:4])
print("colors[:3]:", colors[:3])
print("colors[::-1] (reversed):", colors[::-1])

# 4. Finding the length
print("Length of tuple:", len(colors))

# 5. Basic tuple operations
numbers = (1, 2, 3)
print("Concatenation:", numbers + (4, 5))
print("Repetition:", numbers * 2)
print("'blue' in colors:", "blue" in colors)
print("Count of 'green':", colors.count("green"))
print("Index of 'blue':", colors.index("blue"))
print("Min / Max of numbers:", min(numbers), "/", max(numbers))

# Tuple unpacking
a, b, c = numbers
print("Unpacked:", a, b, c)

# Tuples are immutable
try:
    colors[0] = "black"
except TypeError as e:
    print("Error:", e)
