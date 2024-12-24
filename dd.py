# Program to count the number of digits in a given number
number = input("Enter a number: ")

# Ensure the input is valid (remove '-' for negative numbers)
valid_number = number.lstrip('-')

if valid_number.isdigit():
    digit_count = len(valid_number)
    print(f"The total number of digits in the number {number} is: {digit_count}")
else:
    print("Invalid input! Please enter a valid number.")
