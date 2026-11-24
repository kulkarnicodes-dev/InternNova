# task1_lists.py - Lists in Python

# 1. Creating a list
fruits = ["apple", "banana", "mango", "orange"]
print("Original list:", fruits)

# 2. Accessing elements
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

# 3. Adding elements
fruits.append("grapes")
fruits.insert(1, "kiwi")
fruits.extend(["pear", "papaya"])
print("After adding:", fruits)

# 4. Updating elements
fruits[0] = "green apple"
print("After updating index 0:", fruits)

# 5. Removing elements
fruits.remove("banana")
popped = fruits.pop()
del fruits[1]
print("Popped element:", popped)
print("After removing:", fruits)

# 6. Sorting the list
fruits.sort()
print("Sorted (ascending):", fruits)
fruits.sort(reverse=True)
print("Sorted (descending):", fruits)

# Loop through the list
print("Looping through list:")
for index, item in enumerate(fruits, start=1):
    print(index, "-", item)
