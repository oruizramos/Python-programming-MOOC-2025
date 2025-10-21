"""
# https://programming-25.mooc.fi/part-1/2-information-from-the-user
"""

"""
# Name Twice
"""

name = input("What is your name")
print(name)
print(name)

"""
# Name and exclamation marks
"""

name = input("What is your name?")
print("!" + name + "!" + name + "!")

"""
# Name and address
"""

given_name = input("Given name: ")
family_name = input("Family name: ")
street_address = input("Street address: ")
city_and_postal_code = input("City and postal code: ")
 
print(given_name + " " + family_name) 
print(street_address)
print(city_and_postal_code)

"""
# Fix the code: Utterances
"""

part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")

"""
# Story
"""

name = input("Please type in a name: ")
year = input("Please type in a year: ")

print(name + " is a valiant knight, born in the year " + year + ". One morning " + name + " woke up to an awful racket: a dragon was approaching the village. Only " + name + " could save the village's residents.")
