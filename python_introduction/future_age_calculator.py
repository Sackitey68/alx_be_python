"""
Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

Instructions:

Create a file named future_age_calculator.py.
Prompt the user to input their current age with the question: “How old are you? ”.
Assume the user will input a valid integer value.
Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.
"""

current_age = int(input("How old are you? "))

# Calculate the user;s age in 2050
year_to_2050 = 2050 - 2023
future_age = current_age + year_to_2050

print("In 2050, you will be", year_to_2050, "years old.")
