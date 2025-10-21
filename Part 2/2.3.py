"""
# https://programming-25.mooc.fi/part-2/3-combining-conditions
"""

"""
# Age check
"""

#Common pattern in programming: Conditions are ordered from most specific/restrictive to most general, and let the logic flow naturally.

#Flow:
#If age < 0 → mistake
#Else if age < 5 (we already know it's ≥ 0 here!) → can't write yet
#Else (must be ≥ 5) → normal message


age = int(input("What is your age? "))

if age < 0:
    print("That must be a mistake")
elif age < 5:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")

"""
# Nephews
"""

name = input("Please type in your name: ")

if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You are not a nephew of any character I know of.")    

"""
# Grades and points
"""
points = float(input("How many points [0-100]: "))

if points < 0 or points > 100:
    grade = "impossible!"
elif points < 50:
    grade = "fail"
elif points < 60:
    grade = 1
elif points < 70:
    grade = 2
elif points < 80:
    grade = 3    
elif points < 90:
    grade = 4
else:
    grade = 5
    
print(f"Grade: {grade}")

"""
# FizzBuzz
"""

number = int(input("Number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

"""
# Leap year
"""

year = int(input("Please type in a year: "))
 
#Initial Statement: A year is (usually) not a leap year. A Leap year is an exeption. 
#Most years are not leap years. So assuming a year is not a leap year (False).
#Only if we find an exception do we set it to (True).

leap_year = False

#General programming principle
#Check the most specific conditions first, then the more general ones."
#This avoids special cases being accidentally handled by general rules.
#Makes debugging easier.
#Makes code closer to natural language reasoning.

# Leap year rules:
# Most specific one: Century years divisible by 100 → not leap year, unless divisible by 400.
if year % 100 == 0:        
    if year % 400 == 0:
        leap_year = True
# Most years divisible by 4 → leap year.
elif year % 4 == 0:
    leap_year = True
 
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
 
"""
# Alphabetically in the middle
"""

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# Check which letter is in the middle
if (letter1 > letter2 and letter1 < letter3) or (letter1 > letter3 and letter1 < letter2):
    middle_letter = letter1
elif (letter2 > letter1 and letter2 < letter3) or (letter2 > letter3 and letter2 < letter1):
    middle_letter = letter2
else:
    middle_letter = letter3

print(f"The letter in the middle is {middle_letter}")


"""
# Gift tax calculator
"""
        
value_of_gift = float(input("Value of gift: "))

#lower limits
lower_limit1 = 5000
lower_limit2 = 25000
lower_limit3 = 55000
lower_limit4 = 200000
lower_limit5 = 1000000

#tax at the lower limits
tax_at_lower_limit1 = 100
tax_at_lower_limit2 = 1700
tax_at_lower_limit3 = 4700
tax_at_lower_limit4 = 22100
tax_at_lower_limit5 = 142100

#exceeding tax rate(%)
exceeding_tax_rate1 = 0.08
exceeding_tax_rate2 = 0.10
exceeding_tax_rate3 = 0.12
exceeding_tax_rate4 = 0.15
exceeding_tax_rate5 = 0.17

#Tier 1 formula
tier1 = tax_at_lower_limit1 + (value_of_gift - lower_limit1) * exceeding_tax_rate1
#Tier 2 formula
tier2 = tax_at_lower_limit2 + (value_of_gift - lower_limit2) * exceeding_tax_rate2
#Tier 3 formula
tier3 = tax_at_lower_limit3 + (value_of_gift - lower_limit3) * exceeding_tax_rate3
#Tier 4 formula
tier4 = tax_at_lower_limit4 + (value_of_gift - lower_limit4) * exceeding_tax_rate4
#Tier 5 formula
tier5 = tax_at_lower_limit5 + (value_of_gift - lower_limit5) * exceeding_tax_rate5


if value_of_gift >= lower_limit5:
    print(f"Amount of tax: {tier5} euros")
elif value_of_gift < lower_limit5 and value_of_gift >= lower_limit4:
    print(f"Amount of tax: {tier4} euros")
elif value_of_gift < lower_limit4 and value_of_gift >= lower_limit3:
    print(f"Amount of tax: {tier3} euros")
elif value_of_gift < lower_limit3 and value_of_gift >= lower_limit2:
    print(f"Amount of tax: {tier2} euros")
elif value_of_gift < lower_limit2 and value_of_gift >= lower_limit1:
    print(f"Amount of tax: {tier1} euros")
else:
    print("No tax!")


"""
# Gift tax calculator (Refactored with untaught content)
"""


# Gift Tax Calculator (clean & scalable version)

gift_value = float(input("Value of gift: "))

# Each tuple = (lower_limit, base_tax, rate)
brackets = [
    (5000, 100, 0.08),
    (25000, 1700, 0.10),
    (55000, 4700, 0.12),
    (200000, 22100, 0.15),
    (1000000, 142100, 0.17)
]

if gift_value < 5000:
    print("No tax!")
else:
    # find the correct bracket
    for i, (lower, base_tax, rate) in enumerate(brackets):
        # If it's the last bracket or the value is below the next bracket
        if i == len(brackets) - 1 or gift_value <= brackets[i + 1][0]:
            tax = base_tax + (gift_value - lower) * rate
            print(f"Amount of tax: {tax} euros")
            break