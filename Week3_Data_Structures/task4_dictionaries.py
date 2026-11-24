# task4_dictionaries.py - Student Information Dictionary

# Creating the dictionary
student = {
    "Name": "Aarav Patil",
    "Age": 21,
    "Course": "MCA",
    "City": "Pune"
}
print("Student dictionary:", student)

# Accessing values
print("Name:", student["Name"])
print("Course:", student.get("Course"))
print("Phone (missing key):", student.get("Phone", "Not available"))

# Adding new key-value pairs
student["Email"] = "aarav@example.com"
student["Semester"] = 1
print("After adding:", student)

# Updating values
student["Age"] = 22
student.update({"City": "Mumbai", "Semester": 2})
print("After updating:", student)

# Removing data
removed = student.pop("Email")
del student["Semester"]
print("Removed email:", removed)
print("After removing:", student)

# Displaying keys and values
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Looping through the dictionary
print("Student details:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Other dictionary methods
print("Is 'Name' a key?", "Name" in student)
print("Number of entries:", len(student))
copy_dict = student.copy()
student.clear()
print("After clear():", student)
print("Copy still has data:", copy_dict)

# Nested dictionary
students = {
    101: {"Name": "Aarav Patil", "Marks": 85},
    102: {"Name": "Sneha Joshi", "Marks": 92},
}
print("Nested dictionary:")
for roll, info in students.items():
    print(f"  Roll {roll}: {info['Name']} scored {info['Marks']}")
