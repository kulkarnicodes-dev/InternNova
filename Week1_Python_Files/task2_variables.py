# Task 2: Variables and Data Types

student_name = "Aarav Sharma"        # str
student_age = 21                     # int
cgpa = 8.75                          # float
is_enrolled = True                   # bool
subjects = ["Python", "DBMS", "DSA"] # list
coordinates = (19.99, 73.79)         # tuple
student_info = {"course": "MCA", "year": 1}  # dict
unique_marks = {85, 90, 78}          # set
complex_number = 3 + 4j              # complex
middle_name = None                   # NoneType

variables = {
    "student_name": student_name,
    "student_age": student_age,
    "cgpa": cgpa,
    "is_enrolled": is_enrolled,
    "subjects": subjects,
    "coordinates": coordinates,
    "student_info": student_info,
    "unique_marks": unique_marks,
    "complex_number": complex_number,
    "middle_name": middle_name,
}

print(f"{'Variable':<16}{'Value':<32}Data Type")
print("-" * 70)
for name, value in variables.items():
    print(f"{name:<16}{str(value):<32}{type(value)}")
