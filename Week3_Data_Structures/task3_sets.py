# task3_sets.py - Sets in Python

# 1. Creating a set
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)

# 2. Removing duplicate values
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique = set(numbers)
print("List with duplicates:", numbers)
print("Unique values (set):", unique)

# 3. Adding and removing elements
set_a.add(10)
set_a.update([11, 12])
print("After adding:", set_a)
set_a.remove(10)
set_a.discard(99)   # no error even if the element is missing
print("After removing:", set_a)

# 4. Union
print("Union:", set_a | set_b)

# 5. Intersection
print("Intersection:", set_a & set_b)

# 6. Difference
print("A - B:", set_a - set_b)
print("B - A:", set_b - set_a)
print("Symmetric difference:", set_a ^ set_b)

# Loop through a set
print("Looping through Set B:")
for item in sorted(set_b):
    print(item, end=" ")
print()
