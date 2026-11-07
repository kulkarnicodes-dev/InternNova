# Task 5: Mini Program - Temperature Converter
# Uses variables, input, operators and type casting.

print("===== TEMPERATURE CONVERTER =====")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice (1/2/3): "))
temp = float(input("Enter the temperature: "))

if choice == 1:
    result = (temp * 9 / 5) + 32
    print(f"{temp}°C = {result:.2f}°F")
elif choice == 2:
    result = (temp - 32) * 5 / 9
    print(f"{temp}°F = {result:.2f}°C")
elif choice == 3:
    result = temp + 273.15
    print(f"{temp}°C = {result:.2f} K")
else:
    print("Invalid choice. Please enter 1, 2 or 3.")
