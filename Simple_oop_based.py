# Develop a simple OOP-based Python class Student with attributes like name,roll number,and marks. 
# Implement methods to input and display details.
class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0.0

    def input_details(self):
        self.name = input("Enter student name: ")
        self.roll_number = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))

    def display_details(self):
        print("\n--- Student Details ---")
        print("Name       :", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks      :", self.marks)


# Ask user how many students to input
n = int(input("How many students? "))

# List to store student objects
students = []

# Input student details using a for loop
for i in range(n):
    print(f"\nEnter details for student {i + 1}:")
    s = Student()
    s.input_details()
    students.append(s)

# Display in a single format (table-like)
print("\nAll Student Records:\n")
print(f"{'S.No':<5} {'Name':<15} {'Roll No':<10} {'Marks':<10}")
print("-" * 45)

for i, s in enumerate(students, start=1):
    print(f"{i:<5} {s.name:<15} {s.roll_number:<10} {s.marks:<10.2f}")