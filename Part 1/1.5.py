"""
# https://programming-25.mooc.fi/part-1/5-conditional-statements
"""

"""
# Orwell
"""

number = int(input("Pleasey type in a number: " ))

if number == 1984:
    print("Orwell")

"""
# Absolute Value
"""

number = int(input("Please type in a number: "))
absolute_value = number

if number < 0:
    absolute_value = number * -1
print(f"The absolute value of this number is {absolute_value}")

"""
# Soup or no soup
"""

PORTION_COST = 5.90 # Constant - price is fixed. Hence the CAPS
name = input("Please tell me your name: ")

if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    total_cost = PORTION_COST * portions
    print(f"The total cost is {total_cost}")

print("Next please!")

"""
# Order of magnitude
"""

number = int(input("Please type in a number: "))

if number < 1000:
    print("This number is smaller than 1000")

if number < 100:
    print("This number is smaller than 100")

if number < 10:
    print ("This number is smaller than 10")

print("Thank you!")

"""
# Calculator
"""  

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

addition = number1 + number2
substraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

if operation == "add":
    print(f"{number1} + {number2} = {addition}")

if operation == "subtract":
    print(f"{number1} - {number2} = {substraction}")

if operation == "multiply":
    print(f"{number1} * {number2} = {multiplication}")

if operation == "divide" and number2 != 0:
    print(f"{number1} / {number2} = {division}")


"""
# Temperatures
"""

farenheit = float(input("Please type in a temperature (F): "))
celcius = (farenheit - 32) / (9/5)
print(f"{farenheit} degrees Fahrenheit equals {celcius} degrees Celsius")

if celcius < 0:
    print("Brr! It's cold in here!")

"""
# Daily Wages
"""    

hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day = input("Day of the week: ")

daily_wages = hourly_wage * hours_worked

if day == "Sunday":
    daily_wages *= 2

print(f"Daily wages: {daily_wages} euros")

"""
# Loyalty Bonus
"""   

points = float(input("How many points are on your card? "))

if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
elif points < 100: #At this point in the course, I guess I was not supposed to use elif, but since I already knew Javascript, I decided to use it
    points *= 1.1
    print("Your bonus is 10 %")

print(f"You now have {points} points")


"""
# What to wear tomorrow
"""  

temperature = float(input("What is the weather forecast for tomorrow? "))
rain = input("Will it rain (yes/no)? ")

if temperature < 30:
    print("Wear jeans and a T-shirt")
if temperature <= 20:
    print("I recommend a jumper as well")
if temperature <= 10:
    print("Take a jacket with you")
if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")

"""
# Solving a quadratic equation
""" 

# The square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

from math import sqrt
 
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
 
value_under_radical = b**2 - (4 * a * c)
 
root1 = (-b + sqrt(value_under_radical)) / (2 * a)
root2 = (-b - sqrt(value_under_radical)) / (2 * a)
 
print(f"The roots are {root1} and {root2}")


    




