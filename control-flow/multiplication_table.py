# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for num in range(1, 11):
    print(f"{number} * {num} = {number * number}")
