"""
#https://programming-25.mooc.fi/part-3/3-more-loops
"""

"""
#Multiplication
"""

number = int(input("Please type in a number: "))
# Start the first operand at 1. This represents the "row" in the table.
operand1 = 1

# Outer loop: keep going until operand1 reaches the user’s number.
# Each iteration represents one row of the multiplication table.
while operand1 <= number:

    # For each new row, start the second operand at 1.
    # This represents the "column" in the table.
    operand2 = 1

    # Inner loop: keep going until operand2 reaches the user’s number.
    # Each iteration represents one column for the current row.
    while operand2 <= number:

        # Calculate the product of the current operands.
        # Storing it in a variable improves clarity and maintainability.
        multiplication = operand1 * operand2  
        print(f"{operand1} x {operand2} = {multiplication}")  

        # Move to the next column in this row.
        operand2 += 1

    # Finished all columns for this row.
    # Move to the next row by increasing operand1.
    operand1 += 1

#Without comments

number = int(input("Please type in a number: "))
operand1 = 1

while operand1 <= number:
    operand2 = 1
    while operand2 <= number:
        multiplication = operand1 * operand2  
        print(f"{operand1} x {operand2} = {multiplication}")  
        operand2 += 1
    operand1 += 1

"""
#First letters of words
"""
sentence = input("Please type in a sentence: ") # Prompt the user and store the input string.

# Add a space at the start, to make handling sentence easier
sentence = " " + sentence                   # Prepend a space to the sentence for uniform word detection.

# Searching for indexes which are preceded by spaces
index = 1                                  # Initialize 'index' to 1 to start checking the first character after the added space.
while index < len(sentence):                # Loop as long as the index is within the bounds of the sentence string.
    # Check if the character BEFORE the current index is a space...
    if sentence[index-1] == " " and \
sentence[index] != " ":             # ...AND the character AT the current index is NOT a space (start of a word).
        print(sentence[index])             # If both conditions are true, print the character (the first letter).
    index += 1                             # Increment the index to move to the next character in the sentence.

"""
#Factorial
"""

while True:                             # Start an infinite loop to repeatedly ask for input.
    # Prompt the user, convert input to integer. Note: this will crash on non-number input.
    number = int(input("Please type in a number: ")) 
    if number <= 0:                     # Check if the number is less than or equal to 0.
        break                           # Exit the 'while True' loop if the condition is met.

    factorial = 1                       # Initialize the 'factorial' result variable to 1.
    new = 1                             # Initialize a counter 'new' to 1 for the inner loop.
    while new <= number:                # Start inner loop: run as long as 'new' is less than or equal to the input 'number'.
        factorial *= new                # Multiply 'factorial' by the current value of 'new' (calculating the product).
        new += 1                        # Increment 'new' by 1 to move to the next factor.

    # Print the calculated result using an f-string to embed the variables.
    print(f"The factorial of the number {number} is {factorial}")

print("Thanks and bye!")                # Print the final exit message after the main loop has broken.

"""
#Flip the pairs
"""

number = int(input("Please type in a number: ")) # Prompt user for a number and convert the input to an integer.

index = 1                                       # Initialize the counter variable, starting at 1.
while index + 1 <= number:                      # Loop continues as long as a full pair (index and index+1) fits within the limit.
    print(index + 1)                            # Print the second number of the pair first (the flipped order).
    print(index)                                # Print the first number of the pair second.
    index += 2                                  # Increment index by 2 to jump to the start of the next pair (e.g., from 1 to 3).

if index <= number:                             # After the loop, check if there is a leftover odd number (if 'number' was odd).
    print(index)                                # If so, print that final, single number.

"""
#Taking turns
"""

number = int(input("Please type in a number: ")) # Prompt user for a number and convert the input to an integer.

left = 1                                        # Initialize the 'left' pointer to 1 (the start of the range).
right = number                                  # Initialize the 'right' pointer to the user's input (the end of the range).

while left < right:                             # Loop continues as long as the left pointer is strictly less than the right pointer.
    print(left)                                 # Print the number from the left (smallest remaining number).
    print(right)                                # Print the number from the right (largest remaining number).
    left += 1                                   # Move the left pointer one step towards the center.
    right -= 1                                  # Move the right pointer one step towards the center.

if left == right:                               # After the loop, check if the pointers have met exactly in the middle.
    print(left)                                 # If they meet (meaning the input number was odd), print the middle number.