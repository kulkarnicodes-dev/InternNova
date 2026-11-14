# task2_loops.py
n = int(input("Enter a number N: "))

print("\n1 to N (for loop):")
for i in range(1, n + 1):
    print(i, end=" ")

print("\n\nN to 1 (while loop):")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1

print(f"\n\nMultiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
