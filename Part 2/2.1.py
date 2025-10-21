"""
# https://programming-25.mooc.fi/part-2/1-programming-terminology
"""


"""
# Fix the syntax
"""

number = int(input("Please type in a number: "))

if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")

print(f"{number} must be my lucky number!")
print("Have a nice day!")

"""
# Fix the syntax
"""

word = input("Please type in a word: ")
lenght = len(word)

if lenght > 1:
    print(f"There are {lenght} in the word {word}")

print("Thank you!")

"""
# Typecasting
"""#

number = float(input("Please type in a number: "))

integer = int(number)
decimal = number - integer

print(f"Integer part: {integer}")
print(f"Integer part: {decimal}")


