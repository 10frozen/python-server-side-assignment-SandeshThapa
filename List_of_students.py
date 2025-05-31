# Create a program that takes a list of student names and stores them in a file. Then, read the file and display the contents.

# Ask the number of students
student_num = int (input("How many number of students name you want to enter:"))

# collecting name from the user
student_name = []
for i in range (student_num):
    name = input("Enter the name of students:")
    student_name.append(name)

# write name to a file
with open("student.txt","w") as file:
    for name in student_name:
        file.write(name +"\n")
print("\nStudent names read from file:")

# Read the file and display the content
with open("student.txt","r") as file:
    contents = file.read()
    print(contents)