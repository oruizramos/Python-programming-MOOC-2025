"""
# https://programming-25.mooc.fi/part-4/2-more-functions
""" 

"""
Line
""" 

def line(length, character_string):                     # Define the function 'line' with arguments for length (int) and the character string (str).
    if character_string == "":                          # Check if the input character string is empty.
        char_to_print = "*"                             # If it's empty, set the character to be printed to a star '*'.
    else:                                               # If the string is not empty.
        char_to_print = character_string[0]             # Set the character to be the first character of the input string (using index 0).
    
    # Print the resulting line
    print(char_to_print * length)                       # Use string multiplication to print the chosen character repeated 'length' times.

# testing the function:
if __name__ == "__main__":                              # Standard check: code runs only when the script is executed directly.
    line(7, "%")                                        # Test 1: Length 7, character '%'. Expected: %%%%%%%
    line(10, "LOL")                                     # Test 2: Length 10, character 'L' (first char of "LOL"). Expected: LLLLLLLLLL
    line(3, "")                                         # Test 3: Length 3, empty string uses '*'. Expected: ***

"""
A box of hashes
""" 


def line(length, character_string):                     # Define the function 'line' with arguments for length (int) and the character string (str).
    if character_string == "":                          # Check if the input character string is empty.
        char_to_print = "*"                             # If it's empty, set the character to be printed to a star '*'.
    else:                                               # If the string is not empty.
        char_to_print = character_string[0]             # Set the character to be the first character of the input string (using index 0).
    
    # Print the resulting line
    print(char_to_print * length)                       # Use string multiplication to print the chosen character repeated 'length' times.

def box_of_hashes(height):                              # Define the function 'box_of_hashes' which takes the rectangle's height as an argument.
    i = 0                                               # Initialize a counter variable 'i' to 0.
    while i < height:                                   # Start a loop that runs 'height' number of times (once for each row).
        line(10, "#")                                   # Call the 'line' function to print a line that is 10 characters long, using '#' as the character.
        i += 1                                          # Increment the counter 'i' to move to the next row.

# testing the function:
if __name__ == "__main__":                              # Standard check: code runs only when the script is executed directly.
    line(7, "%")                                        # Test 1 for 'line': Length 7, character '%'. Expected: %%%%%%%
    line(10, "LOL")                                     # Test 2 for 'line': Length 10, character 'L'. Expected: LLLLLLLLLL
    line(3, "")                                         # Test 3 for 'line': Length 3, empty string uses '*'. Expected: ***
    
    print()                                             # Print an empty line for visual separation in the output.
    
    box_of_hashes(5)                                    # Test 1 for 'box_of_hashes': Print a rectangle 5 rows high.
    print()                                             # Print an empty line for visual separation.
    box_of_hashes(2)                                    # Test 2 for 'box_of_hashes': Print a rectangle 2 rows high.

"""
A square of hashes
""" 
def line(length, character_string):                     # Define the function 'line' with arguments for length (int) and the character string (str).
    if character_string == "":                          # Check if the input character string is empty.
        char_to_print = "*"                             # If it's empty, set the character to be printed to a star '*'.
    else:                                               # If the string is not empty.
        char_to_print = character_string[0]             # Set the character to be the first character of the input string (using index 0).
    
    # Print the resulting line
    print(char_to_print * length)                       # Use string multiplication to print the chosen character repeated 'length' times.

def box_of_hashes(height):                              # Define the function 'box_of_hashes' which takes the rectangle's height as an argument.
    i = 0                                               # Initialize a counter variable 'i' to 0.
    while i < height:                                   # Start a loop that runs 'height' number of times (once for each row).
        line(10, "#")                                   # Call the 'line' function to print a line that is 10 characters long, using '#' as the character.
        i += 1                                          # Increment the counter 'i' to move to the next row.

def square_of_hashes(size):                             # Define the function 'square_of_hashes' which takes the side length as an argument.
    i = 0                                               # Initialize a counter 'i' for the rows.
    while i < size:                                     # Start a loop that runs 'size' times (for the height of the square).
        line(size, "#")                                 # Call 'line' to print a row that is 'size' characters long using '#'.
        i += 1                                          # Increment the row counter 'i'.

# testing the function:
if __name__ == "__main__":                              # Standard check: code runs only when the script is executed directly.
    line(7, "%")                                        # Test 1 for 'line': Length 7, character '%'. Expected: %%%%%%%
    line(10, "LOL")                                     # Test 2 for 'line': Length 10, character 'L'. Expected: LLLLLLLLLL
    line(3, "")                                         # Test 3 for 'line': Length 3, empty string uses '*'. Expected: ***
    
    print()                                             # Print an empty line for visual separation in the output.
    
    box_of_hashes(5)                                    # Test 1 for 'box_of_hashes': Print a rectangle 5 rows high.
    print()                                             # Print an empty line for visual separation.
    box_of_hashes(2)                                    # Test 2 for 'box_of_hashes': Print a rectangle 2 rows high.

    print()                                             # Print an empty line for visual separation.

    square_of_hashes(5)                                 # Test 1 for 'square_of_hashes': Print a 5x5 hash square.
    print()                                             # Print an empty line for visual separation.
    square_of_hashes(3)                                 # Test 2 for 'square_of_hashes': Print a 3x3 hash square.


"""
A square
""" 

def line(length, character_string):                     # Define the function 'line' with arguments for length (int) and the character string (str).
    if character_string == "":                          # Check if the input character string is empty.
        char_to_print = "*"                             # If it's empty, set the character to be printed to a star '*'.
    else:                                               # If the string is not empty.
        char_to_print = character_string[0]             # Set the character to be the first character of the input string (using index 0).
    
    # Print the resulting line
    print(char_to_print * length)                       # Use string multiplication to print the chosen character repeated 'length' times.

def box_of_hashes(height):                              # Define the function 'box_of_hashes' which takes the rectangle's height as an argument.
    i = 0                                               # Initialize a counter variable 'i' to 0.
    while i < height:                                   # Start a loop that runs 'height' number of times (once for each row).
        line(10, "#")                                   # Call the 'line' function to print a line that is 10 characters long, using '#' as the character.
        i += 1                                          # Increment the counter 'i' to move to the next row.

def square_of_hashes(size):                             # Define the function 'square_of_hashes' which takes the side length as an argument.
    i = 0                                               # Initialize a counter 'i' for the rows.
    while i < size:                                     # Start a loop that runs 'size' times (for the height of the square).
        line(size, "#")                                 # Call 'line' to print a row that is 'size' characters long using '#'.
        i += 1                                          # Increment the row counter 'i'.

def square(size, character):                            # Define the function 'square' with size (int) and character (str) arguments.
    i = 0                                               # Initialize a counter 'i' for the rows.
    while i < size:                                     # Start a loop that runs 'size' times (for the height of the square).
        line(size, character)                           # Call 'line' to print a row of length 'size' using the provided 'character'.
        i += 1                                          # Increment the row counter 'i'.

# testing the function:
if __name__ == "__main__":                              # Standard check: code runs only when the script is executed directly.
    line(7, "%")                                        # Test 1 for 'line': Length 7, character '%'. Expected: %%%%%%%
    line(10, "LOL")                                     # Test 2 for 'line': Length 10, character 'L'. Expected: LLLLLLLLLL
    line(3, "")                                         # Test 3 for 'line': Length 3, empty string uses '*'. Expected: ***
    
    print()                                             # Print an empty line for visual separation in the output.
    
    box_of_hashes(5)                                    # Test 1 for 'box_of_hashes': Print a rectangle 5 rows high.
    print()                                             # Print an empty line for visual separation.
    box_of_hashes(2)                                    # Test 2 for 'box_of_hashes': Print a rectangle 2 rows high.

    print()                                             # Print an empty line for visual separation.

    square_of_hashes(5)                                 # Test 1 for 'square_of_hashes': Print a 5x5 hash square.
    print()                                             # Print an empty line for visual separation.
    square_of_hashes(3)                                 # Test 2 for 'square_of_hashes': Print a 3x3 hash square.

    print()                                             # Print an empty line for visual separation.

    square(5, "*")                                      # Test 1 for 'square': Print a 5x5 square using '*'.
    print()                                             # Print an empty line for visual separation.
    square(3, "o")                                      # Test 2 for 'square': Print a 3x3 square using 'o'.


"""
A triangle
""" 
def line(length, character_string):                     # Define the function 'line' with arguments for length (int) and the character string (str).
    if character_string == "":                          # Check if the input character string is empty.
        char_to_print = "*"                             # If it's empty, set the character to be printed to a star '*'.
    else:                                               # If the string is not empty.
        char_to_print = character_string[0]             # Set the character to be the first character of the input string (using index 0).
    
    # Print the resulting line
    print(char_to_print * length)                       # Use string multiplication to print the chosen character repeated 'length' times.

def box_of_hashes(height):                              # Define the function 'box_of_hashes' which takes the rectangle's height as an argument.
    i = 0                                               # Initialize a counter variable 'i' to 0.
    while i < height:                                   # Start a loop that runs 'height' number of times (once for each row).
        line(10, "#")                                   # Call the 'line' function to print a line that is 10 characters long, using '#' as the character.
        i += 1                                          # Increment the counter 'i' to move to the next row.

def square_of_hashes(size):                             # Define the function 'square_of_hashes' which takes the side length as an argument.
    i = 0                                               # Initialize a counter 'i' for the rows.
    while i < size:                                     # Start a loop that runs 'size' times (for the height of the square).
        line(size, "#")                                 # Call 'line' to print a row that is 'size' characters long using '#'.
        i += 1                                          # Increment the row counter 'i'.

def square(size, character):                            # Define the function 'square' with size (int) and character (str) arguments.
    i = 0                                               # Initialize a counter 'i' for the rows.
    while i < size:                                     # Start a loop that runs 'size' times (for the height of the square).
        line(size, character)                           # Call 'line' to print a row of length 'size' using the provided 'character'.
        i += 1                                          # Increment the row counter 'i'.

def triangle(size):                                     # Define the function 'triangle' that takes the height/base 'size'.
    i = 1                                               # Initialize a counter 'i' to 1 (representing the length of the first row).
    while i <= size:                                    # Loop as long as the current row length 'i' is less than or equal to 'size'.
        line(i, "#")                                    # Call 'line' to print a hash line of length 'i'.
        i += 1                                          # Increment 'i' to increase the length of the next row.

# testing the function:
if __name__ == "__main__":                              # Standard check: code runs only when the script is executed directly.
    line(7, "%")                                        # Test 1 for 'line': Length 7, character '%'. Expected: %%%%%%%
    line(10, "LOL")                                     # Test 2 for 'line': Length 10, character 'L'. Expected: LLLLLLLLLL
    line(3, "")                                         # Test 3 for 'line': Length 3, empty string uses '*'. Expected: ***
    
    print()                                             # Print an empty line for visual separation in the output.
    
    box_of_hashes(5)                                    # Test 1 for 'box_of_hashes': Print a rectangle 5 rows high.
    print()                                             # Print an empty line for visual separation.
    box_of_hashes(2)                                    # Test 2 for 'box_of_hashes': Print a rectangle 2 rows high.

    print()                                             # Print an empty line for visual separation.

    square_of_hashes(5)                                 # Test 1 for 'square_of_hashes': Print a 5x5 hash square.
    print()                                             # Print an empty line for visual separation.
    square_of_hashes(3)                                 # Test 2 for 'square_of_hashes': Print a 3x3 hash square.

    print()                                             # Print an empty line for visual separation.

    square(5, "*")                                      # Test 1 for 'square': Print a 5x5 square using '*'.
    print()                                             # Print an empty line for visual separation.
    square(3, "o")                                      # Test 2 for 'square': Print a 3x3 square using 'o'.

    print()                                             # Print an empty line for visual separation.

    triangle(6)                                         # Test 1 for 'triangle': Print a triangle with height/base 6.
    print()                                             # Print an empty line for visual separation.
    triangle(3)                                         # Test 2 for 'triangle': Print a triangle with height/base 3.


"""
A shape
""" 

def line(length, character_string):                     # Define the function 'line' with arguments for length (int) and the character string (str).
    if character_string == "":                          # Check if the input character string is empty.
        char_to_print = "*"                             # If it's empty, set the character to be printed to a star '*'.
    else:                                               # If the string is not empty.
        char_to_print = character_string[0]             # Set the character to be the first character of the input string (using index 0).
    
    # Print the resulting line
    print(char_to_print * length)                       # Use string multiplication to print the chosen character repeated 'length' times.

def box_of_hashes(height):                              # Define the function 'box_of_hashes' which takes the rectangle's height as an argument.
    i = 0                                               # Initialize a counter variable 'i' to 0.
    while i < height:                                   # Start a loop that runs 'height' number of times (once for each row).
        line(10, "#")                                   # Call the 'line' function to print a line that is 10 characters long, using '#' as the character.
        i += 1                                          # Increment the counter 'i' to move to the next row.

def square_of_hashes(size):                             # Define the function 'square_of_hashes' which takes the side length as an argument.
    i = 0                                               # Initialize a counter 'i' for the rows.
    while i < size:                                     # Start a loop that runs 'size' times (for the height of the square).
        line(size, "#")                                 # Call 'line' to print a row that is 'size' characters long using '#'.
        i += 1                                          # Increment the row counter 'i'.

def square(size, character):                            # Define the function 'square' with size (int) and character (str) arguments.
    i = 0                                               # Initialize a counter 'i' for the rows.
    while i < size:                                     # Start a loop that runs 'size' times (for the height of the square).
        line(size, character)                           # Call 'line' to print a row of length 'size' using the provided 'character'.
        i += 1                                          # Increment the row counter 'i'.

def triangle(size):                                     # Define the function 'triangle' that takes the height/base 'size'.
    i = 1                                               # Initialize a counter 'i' to 1 (representing the length of the first row).
    while i <= size:                                    # Loop as long as the current row length 'i' is less than or equal to 'size'.
        line(i, "#")                                    # Call 'line' to print a hash line of length 'i'.
        i += 1                                          # Increment 'i' to increase the length of the next row.

def shape(tri_size, tri_char, rect_height, rect_char):   # Define the function 'shape' with four specific arguments.
    # Print the Triangle part
    i = 1                                               # Initialize a counter 'i' to 1 for the triangle rows.
    while i <= tri_size:                                # Loop as long as the current row length 'i' is within the triangle size.
        line(i, tri_char)                               # Call 'line' to print a line of length 'i' using the triangle character.
        i += 1                                          # Increment 'i' to increase the length of the next row.

    # Print the Rectangle part
    i = 0                                               # Reset counter 'i' to 0 for the rectangle rows.
    while i < rect_height:                              # Loop as long as the counter 'i' is less than the rectangle height.
        line(tri_size, rect_char)                       # Call 'line' to print a line of width 'tri_size' using the rectangle character.
        i += 1                                          # Increment 'i' to move to the next row.

# testing the function:
if __name__ == "__main__":                              # Standard check: code runs only when the script is executed directly.
    line(7, "%")                                        # Test 1 for 'line': Length 7, character '%'. Expected: %%%%%%%
    line(10, "LOL")                                     # Test 2 for 'line': Length 10, character 'L'. Expected: LLLLLLLLLL
    line(3, "")                                         # Test 3 for 'line': Length 3, empty string uses '*'. Expected: ***
    
    print()                                             # Print an empty line for visual separation in the output.
    
    box_of_hashes(5)                                    # Test 1 for 'box_of_hashes': Print a rectangle 5 rows high.
    print()                                             # Print an empty line for visual separation.
    box_of_hashes(2)                                    # Test 2 for 'box_of_hashes': Print a rectangle 2 rows high.

    print()                                             # Print an empty line for visual separation.

    square_of_hashes(5)                                 # Test 1 for 'square_of_hashes': Print a 5x5 hash square.
    print()                                             # Print an empty line for visual separation.
    square_of_hashes(3)                                 # Test 2 for 'square_of_hashes': Print a 3x3 hash square.

    print()                                             # Print an empty line for visual separation.

    square(5, "*")                                      # Test 1 for 'square': Print a 5x5 square using '*'.
    print()                                             # Print an empty line for visual separation.
    square(3, "o")                                      # Test 2 for 'square': Print a 3x3 square using 'o'.

    print()                                             # Print an empty line for visual separation.

    triangle(6)                                         # Test 1 for 'triangle': Print a triangle with height/base 6.
    print()                                             # Print an empty line for visual separation.
    triangle(3)                                         # Test 2 for 'triangle': Print a triangle with height/base 3.

    print()                                             # Print an empty line for visual separation.

    shape(5, "X", 3, "*")                               # Test 1 for 'shape': 5x5 'X' triangle, 5x3 '*' rectangle.
    print()                                             # Print an empty line for visual separation.
    shape(2, "o", 4, "+")                               # Test 2 for 'shape': 2x2 'o' triangle, 2x4 '+' rectangle.
    print()                                             # Print an empty line for visual separation.
    shape(3, ".", 0, ",")                               # Test 3 for 'shape': 3x3 '.' triangle, 3x0 ',' rectangle (zero height).


"""
A spruce
""" 

#### Solution with for loop


def spruce(size):
    print("a spruce!")

    # 1. Calculate the total width of the base of the tree
    # This determines how wide the pattern needs to be for centering.
    total_width = 2 * size - 1

    # 2. Print the branches (from 1 to 'size' rows)
    # The loop variable 'i' represents the current row number (starting from 1).
    for i in range(1, size + 1):
        # Number of asterisks in this row: 2*i - 1 (1, 3, 5, 7, ...)
        num_stars = 2 * i - 1

        # Calculate the number of spaces needed for centering:
        # (Total Width - Current Stars) / 2
        num_spaces = (total_width - num_stars) // 2

        # Construct and print the line
        line = " " * num_spaces + "*" * num_stars
        print(line)

    # 3. Print the trunk (a single asterisk, centered)
    # The trunk always has a width of 1.
    trunk_width = 1
    trunk_spaces = (total_width - trunk_width) // 2
    
    trunk_line = " " * trunk_spaces + "*" * trunk_width
    print(trunk_line)

# Example calls to demonstrate the function as requested:
print("--- spruce(3) output ---")
spruce(3)
print("--- spruce(5) output ---")
spruce(5)

##### SOlution with while loop


def spruce(size):                                       # Define the function 'spruce' which takes one argument, 'size'.
    print("a spruce!")                                  # Print the required introductory text.
    
    # 1. Print the tree leaves (the triangle part)
    i = 1                                               # Initialize row counter 'i' starting from 1.
    while i <= size:                                    # Loop 'size' number of times (for the height of the leaves).
        stars = 2 * i - 1                               # Calculate the number of stars for the current row (1, 3, 5, ...).
        spaces = size - i                               # Calculate the number of leading spaces needed for centering.
        print(" " * spaces + "*" * stars)               # Print the calculated spaces followed by the stars.
        i += 1                                          # Increment 'i' to move to the next, wider row.

    # 2. Print the trunk
    trunk_spaces = size - 1                             # Calculate the spaces needed to center the single '*' trunk.
    print(" " * trunk_spaces + "*")                     # Print the centered trunk.

if __name__ == "__main__":                              # Standard check: code runs only when the script is executed directly.
    spruce(3)                                           # Test 1: Print a spruce tree of size 3.
    print()                                             # Print an empty line for visual separation.
    spruce(5)                                           # Test 2: Print a spruce tree of size 5.


"""
The greatest number
""" 
def greatest_number(num1, num2, num3):             # Define the function 'greatest_number' with three arguments.
    if num1 >= num2 and num1 >= num3:              # Check if the first number is greater than or equal to the second AND the third.
        return num1                                # If it is, then num1 is the greatest, so we return it.
    elif num2 >= num1 and num2 >= num3:            # Otherwise, check if the second number is greater than or equal to the first AND the third.
        return num2                                # If it is, then num2 is the greatest, so we return it.
    else:                                          # If neither of the first two checks were true.
        return num3                                # The third number (num3) must be the greatest, so we return it.

if __name__ == "__main__":                         # Standard block for testing the function when the script is run directly.
    print(greatest_number(3, 4, 1))                # Test 1: Expected output is 4.
    print(greatest_number(99, -4, 7))               # Test 2: Expected output is 99.
    print(greatest_number(0, 0, 0))                # Test 3: Expected output is 0.

"""
Same characters
""" 

def same_chars(text, index1, index2):               # Define the function with string 'text' and two integer indices.
    length = len(text)                              # Get the length of the string to use for boundary checks.

    # Check for invalid indices (out of bounds)
    if index1 < 0 or index1 >= length:              # Check if index1 is less than 0 OR greater than or equal to length.
        return False                                # If index1 is invalid, return False.
    if index2 < 0 or index2 >= length:              # Check if index2 is less than 0 OR greater than or equal to length.
        return False                                # If index2 is invalid, return False.

    # If both indices are valid, compare the characters
    return text[index1] == text[index2]             # Return True if characters match, False otherwise.

if __name__ == "__main__":                          # Standard block for testing the function when the script is run directly.
    # same characters m and m
    print(same_chars("programmer", 6, 7))           # Test 1: Expected output is True.
    # different characters p and r
    print(same_chars("programmer", 0, 4))           # Test 2: Expected output is False.
    # the second index is not within the string
    print(same_chars("programmer", 0, 12))          # Test 3: Expected output is False.

"""
First, second and last words
""" 

def first_word(text):                           # Define the function to get the first word, taking a string 'text'.
    words = text.split(" ")                     # Split the sentence into a list of words using the space character.
    return words[0]                             # Return the element at index 0, which is always the first word.

def second_word(text):                          # Define the function to get the second word, taking a string 'text'.
    words = text.split(" ")                     # Split the sentence into a list of words.
    return words[1]                             # Return the element at index 1, which is always the second word.

def last_word(text):                            # Define the function to get the last word, taking a string 'text'.
    words = text.split(" ")                     # Split the sentence into a list of words.
    return words[-1]                            # Return the element at index -1, which is always the last word in Python.

if __name__ == "__main__":                      # Standard check: code runs only when the script is executed directly.
    sentence = "it was a dark and stormy python"# Define the test sentence string.
    print(first_word(sentence))                 # Test 1: Get and print the first word ("it").
    print(second_word(sentence))                # Test 2: Get and print the second word ("was").
    print(last_word(sentence))                  # Test 3: Get and print the last word ("python").
    
    sentence2 = "it was"                        # Define a shorter test sentence.
    print(second_word(sentence2))               # Test 4: Get and print the second word ("was").
    print(last_word(sentence2))                 # Test 5: Get and print the last word ("was").