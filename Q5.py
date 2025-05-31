# Write Python code to read from a CSV file of student marks and calculate average marks.
import csv

total_sum = 0
total_count = 0

with open('marks.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        marks = [int(m) for m in row[1:]]
        average = sum(marks) / len(marks)
        print(f"{name}'s average: {average:.2f}")

        # Add to total for class average
        total_sum += sum(marks)
        total_count += len(marks)

# Class average
class_average = total_sum / total_count
print(f"\nClass average: {class_average:.2f}")
