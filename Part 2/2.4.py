"""
# https://programming-25.mooc.fi/part-2/4-simple-loops
"""

"""
# Shall we continue
"""

while True: 
    print("hi")
    answer = input("Shall we continue? ")
    if answer == "no":
        break

print("okay then")

"""
# Input validation
"""

from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        break
    if number > 0:
        print(sqrt(number))
    else:
        print("Invalid number")

print("Exiting...")

#logic flow:

#while True:
#    value = ...
#    if exit_condition:
#        break
#    do something useful


#Immediately handles the “exit condition” (if number == 0: break), so the rest of the loop doesn’t need to worry about it.
#Simpler branching: Only two outcomes left — positive or negative.
#Better structure: The “Exiting…” message is printed after the loop ends, which conceptually makes more sense (you exit first, then announce it).

"""
# Fix the code: Countdown
"""

number = 5
print("Countdown!")

while True:
  print(number)
  number -= 1
  if number == 0:
    break

print("Now!")

"""
# Repeat password
"""

password = input("Password: ")

while True:
    repeat = input("Repeat password: ")
    if repeat == password:
        break
    print("They do not match!")

print("User account created!")


