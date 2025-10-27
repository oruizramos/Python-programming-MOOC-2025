"""
# https://programming-25.mooc.fi/part-3/4-defining-functions
"""

"""
# Seven Brothers
"""

def seven_brothers():                               # Define a function named seven_brothers that takes no arguments.
    print("Aapo")                                   
    print("Eero")                                   
    print("Juhani")                                 
    print("Lauri")                                  
    print("Simeoni")                                
    print("Timo")                                   
    print("Tuomas")                                 
if __name__ == "__main__":                          # Check if the script is being run directly.
    seven_brothers()                                # Call the function to execute the printing.

"""
# The first character
"""

def first_character(text):                              # Define the function, accepting one string argument named 'text'.
    print(text[0])                                      # Print the character at index 0 (the first character) of the string.
if __name__ == "__main__":                              # Check if the script is being executed directly.
    first_character('night')                            # Call the function with the string 'night' (this will print 'n').

"""
# Mean
""" 

def mean(number1, number2, number3):                     # Define the function, accepting three arguments.
    answer = (number1 + number2 + number3) / 3          # Calculate the sum, divide by 3, and store the result (the mean) in 'answer'.
    print(answer)                                       # Print the final calculated mean.

if __name__ == "__main__":                              # Check if the script is being run directly.
    mean(1, 2, 3)                                      # Call the function with 1, 2, and 3 (the output will be 2.0).

"""
# Print many times
""" 

def print_many_times(text, times):                      # Define the function, accepting the string 'text' and the integer 'times'.
    while times > 0:                                    # Start a loop that continues as long as 'times' is greater than 0.
        print(text)                                     # Print the input string 'text'.
        times -= 1                                      # Decrement 'times' by 1 in each iteration to move towards the loop exit condition.

if __name__ == "__main__":                              # Check if the script is being run directly.
    print_many_times("python", 5)                       # Test the function by printing "python" 5 times.


"""
# A square of hashes
""" 

def hash_square(size):                                   # Define the function, taking 'size' (the side length) as an argument.
    tows = size                                         # Initialize a counter variable 'tows' (representing rows remaining) to 'size'.
    while tows > 0:                                     # Start a loop that continues as long as there are rows left to print (tows > 0).
        print("#" * size)                               # Print a row by multiplying the '#' character by the side 'size'.
        tows -= 1                                       # Decrement the row counter 'tows' by 1 to move toward the loop exit condition.

if __name__ == "__main__":                              # Check if the script is being executed directly.
    hash_square(5)                                      # Test the function by drawing a square with side length 5.



"""
# Chessboard
""" 

def chessboard(size):                                   # Define the function, taking 'size' as the side length of the board.
    i = 0                                               # Initialize row counter 'i' to 0.
    while i < size:                                     # Loop continues as long as the current row index 'i' is less than the 'size'.
        if i % 2 == 0:                                  # Check if the current row index 'i' is even (0, 2, 4...).
            row = "10"*size                             # If even, create a long string of "10" repeated 'size' times.
        else:                                           # Otherwise (if the current row index 'i' is odd: 1, 3, 5...).
            row = "01"*size                             # If odd, create a long string of "01" repeated 'size' times.
        # Remove extra characters at the end of the row
        print(row[0:size])                              # Print only the first 'size' characters of the generated string (the correct row length).
        i += 1                                          # Increment the row counter 'i' by 1.

# testing the function:
if __name__ == "__main__":                              # Check if the script is being run directly.
    chessboard(6)                                       # Test the function by generating a 6x6 chessboard.

"""
# A word squared
""" 

def squared(characters, size):                          # Define the function, accepting the string 'characters' and the square 'size'.
    i = 0                                               # Initialize counter 'i' to 0; this tracks the current character's global position.
    row = ""                                            # Initialize an empty string to build the current row.
    while i < size * size:                              # Loop as long as the global position 'i' is less than the total characters needed (size * size).
        if i > 0 and i % size == 0:                     # Check if 'i' is greater than 0 AND is a multiple of 'size' (meaning a row is complete).
            print(row)                                  # Print the completed row string.
            row = ""                                    # Reset the row string for the next line.
        
        # Calculate the index to cycle through the input string
        char_index = i % len(characters)                # Use modulo division to cycle the index through the length of 'characters'.
        row += characters[char_index]                   # Append the next character (from the input string) to the current row.
        i += 1                                          # Increment the global position counter 'i'.
    
    print(row)                                          # After the loop finishes, print the final remaining row.

# testing the function:
if __name__ == "__main__":                              # Standard check to ensure code runs when script is executed directly.
    print("Test 1: 'ab', 3x3")                          # Label the first test case.
    squared("ab", 3)                                    # Test the function with "ab" and size 3.
    print()                                             # Print an empty line for spacing.
    print("Test 2: 'aybabtu', 5x5")                     # Label the second test case.
    squared("aybabtu", 5)                               # Test the function with "aybabtu" and size 5.
