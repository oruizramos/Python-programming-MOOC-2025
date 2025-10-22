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


"""
# Pin and number of attempts
"""
#Track attempts
attempts = 0

#Loop core. Infinite loop that will keep asking for the PIN.
while True:

#Exception(break) condition
    PIN = int(input("PIN: ")) #Ask the user to enter a PIN number.
    attempts += 1 # Each time the user types something, we count that as one attempt.
    if PIN == 4321: #Check if the entered PIN is correct.
        break # If it's correct, we stop the loop using 'break'.

#Otherwise... (Negative outcome print)
    print("Wrong")

#(Positive outcome prints)    
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")

"""
# The next leap year
"""

year = int(input("Year: "))
start_year = year

while True:
    year += 1
    # Leap year rules (Once again, exception FIRST, then generality... because programming logic)
    # A leap year is a year that is divisible by 400, or divisible by 4 but not by 100.
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        break

print(f"The next leap year after {start_year} is {year}")


"""
# Story
"""

story = ""
last_word = ""

#Loop Rule: CPU “Check (Conditions) first, Process second, Update state(Remember) last” 
#Whenever a loop:
#1. Receives input or iterates over something
#2. Checks conditions
#3. Updates some state variables

#1. Check conditions first
#2. Action/Do current taks
#3. Update state

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == last_word:    # 1. Check conditions first
        break
    story += word + " "                       # 2. Process (current word)
    last_word = word                          # 3. Update state (For next iteration)
 
print(story)
 
"""
# Working with numbers
"""

print("Please type in integer numbers. Type in 0 to finish.")

# Initialize tracker variables (all declared at the top for organization)
count = 0        
total = 0        
positives = 0    
negatives = 0    

# infinite loop to continuously ask the user for input
while True:
    # Get the number from the user
    number = int(input("Number: "))
    #CPU
    # Check first: stopping condition (exception) 
    # If the user entered 0, we stop immediately and do not process this number
    if number == 0:
        break

    # Process / Update state: this is only executed if number != 0
    count += 1         # increment the count of numbers entered
    total += number    # add the number to the total sum

    # Update additional state: count positives and negatives
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1

# Calculate derived value (mean) after all input has been processed. Not added at the start because of the following:
    #Declaration: Top of program — good for organization
    #Calculation: When needed — better efficiency and clearer logic
mean = total / count   

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")

