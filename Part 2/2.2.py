"""
# https://programming-25.mooc.fi/part-2/2-else-elif
"""


"""
# Age of maturity
"""

age = int(input("How old are you? "))

age_of_maturity = 18

if age >= age_of_maturity:
    print("You are of age!")
else:
    print("You are not of age!")

"""
# Greater than or equal to
"""

number1 = float(input("Please type in a number: "))
number2 = float(input("Please type in another number: "))

if number1 > number2:
    print(f"The greater number was: {number1}")
elif number2 > number1:
    print(f"The greater number was: {number2}")
else:
    print(f"The numbers are equal!")


"""
# The elder
"""

person1 = input("Person's 1 name: ")
age1 = int(input("Person's 1 age: "))
person2 = input("Person's 2 name: ")
age2 = int(input("Person's 2 age: "))

if age1 > age2:
    print(f"The elder is {person1}")
elif age2 > age1:
    print(f"The elder is {person2}")
else:
    print(f"{person1} and {person2} are the same age")

"""
# Alphabetically last
"""

word1 = input("Please type in a word: ")
word2 = input("Please type in another word: ")

if word1 > word2:
    print(f"{word1} comes alphabetically last")
elif word2 > word1:
    print(f"{word2} comes alphabetically last")
else:
    print("You gave the same word twice")