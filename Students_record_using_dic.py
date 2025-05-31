# Implement a program to store student records (name, roll, marks,contact number) using a dictionary.
# a. Provide menu options to add, search, and display students

# Simple Student Record System using Dictionary
students = {}

while True:
    print("\n--- Student Record Menu ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        contact = input("Enter contact number: ")
        students[roll] = [name, marks, contact]
        print("Student added.")

    elif choice == '2':
        roll = input("Enter roll number to search: ")
        if roll in students:
            print("Name:", students[roll][0])
            print("Marks:", students[roll][1])
            print("Contact:", students[roll][2])
        else:
            print("Student not found.")

    elif choice == '3':
        if students:
            for roll, data in students.items():
                print(f"Roll: {roll}, Name: {data[0]}, Marks: {data[1]}, Contact: {data[2]}")
        else:
            print("No records to display.")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
