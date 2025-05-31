#Create a Python function to calculate factorial of a number using recursion.
def factorial(n):
    if n < 0:
        print("Negative values aren't allowed.")
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

number = int(input("Enter a number: "))
fact = factorial(number)
print(f"Factorial of {number}: {fact}")