#####
# https://programming-25.mooc.fi/part-1/4-arithmetic-operations
######

#####
# Times five
######

number = input("Please type in a number: ")
result = int(number) * 5
print(f"{number} times 5 is {result}")

#####
# Names and age
######

name = input("What is your name?")
born_year = int(input("Which year were you born?"))
age = 2021 - born_year

print(f"Hi {name}, you will be {age} years old at the end of the year 2021")

#####
# Seconds in a day
######

days = int(input("How many days? "))
seconds = days * 24 * 60 * 60  # hours * minutes * seconds

print(f"Seconds in that many days: {seconds}")

#####
# FIX THE CODE: PRODUCT
######

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print(f"The product is {product}")

#####
# SUM AND PRODUCT
######

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

addition = number1 + number2
product = number1 * number2

print(f"The sum of the numbers: {addition}")
print(f"The product of the numbers: {product}")

#####
# SUM AND MEAN
######

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
number4 = int(input("Number 4: "))

addition = number1 + number2 + number3+ number4
mean = addition / 4

print(f"The sum of the numbers is {addition} and the mean is {mean}")


#####
# FOOD EXPENDITURE
######

times_in_cafeteria = int(input("How many times a week do you eat at the student cafeteria?"))
price_student_lunch = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

cafeteria_weekly = times_in_cafeteria * price_student_lunch

weekly_total = groceries + cafeteria_weekly
daily_total = weekly_total / 7

print("Average food expenditure: ")
print(f"Daily: {daily_total} euros")
print(f"Weekly: {weekly_total} euros")

#####
# Students in groups
######

students = int(input("How many students on the course? "))
desired_size = int(input("Desired group size? "))

number_of_groups = students // desired_size

if students % desired_size > 0:
    number_of_groups += 1

print(f"Number of groups formed: {number_of_groups}")