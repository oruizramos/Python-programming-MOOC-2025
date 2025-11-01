"""
https://programming-25.mooc.fi/part-4/4-definite-iteration
""" 

"""
Start-studded
""" 

input_string = input("Please type in a string: ")  # Prompt the user to enter a string and store it.

# Iterate through each character in the input string.
for character in input_string:                      # Start a 'for' loop that processes one 'character' at a time.
    print(character)                               # Print the current character from the string.
    print("*")                                     # Print an asterisk on the very next line.

"""
From negative to positive
""" 

number = int(input("Please type in a positive integer: ")) # Get N from user, convert to integer.

# Loop from -N up to and including N (N+1 makes the range inclusive).
for i in range(-number, number + 1): # Iterate through the range [-N, N].
    if i == 0:                       # Check if the current number is zero.
        continue                     # Skip the rest of the loop for 0.
    
    print(i)                         # Print all non-zero numbers.

"""
List of stars
""" 

def list_of_stars(my_list):               # Define the function taking one list argument.
    for number in my_list:                # Loop through each 'number' in the input list.
        print("*" * number)               # Print a line of stars, repeating "*" by the value of 'number'.

if __name__ == "__main__":                # Check if the script is run directly.
    # Test case 1
    list_of_stars([3, 7, 1, 1, 2])        # Call the function with a sample list.
    print()                               # Print a blank line for separation.
    
    # Test case 2
    list_of_stars([1, 2, 3])              # Another test case.


"""
Anagrams
""" 

def anagrams(string1, string2):               # Define function taking two strings.
    return sorted(string1) == sorted(string2) # Sort both strings and check if the resulting lists are equal.

if __name__ == "__main__":                    # Test block execution.
    # Test cases from the problem
    print(anagrams("tame", "meta"))           # True
    print(anagrams("tame", "mate"))           # True
    print(anagrams("tame", "team"))           # True
    print(anagrams("tabby", "batty"))         # False
    print(anagrams("python", "java"))         # False
    
    # Additional test case
    print(anagrams("listen", "silent"))       # True


"""
Palindromes
""" 

def palindromes(text):                       # Define the function to check for palindromes.
    return text == text[::-1]               # Return True if the string equals its reverse (text[::-1]).

# Main program loop starts here (outside the __main__ block).
while True:                                  # Start an infinite loop to repeatedly ask for input.
    word = input("Please type in a palindrome: ") # Prompt the user for a word.
    
    if palindromes(word):                    # Check if the entered word is a palindrome using the function.
        print(f"{word} is a palindrome!")    # If True, print success message.
        break                                # Exit the loop, ending the program.
    else:                                    # If the word is not a palindrome.
        print("that wasn't a palindrome")    # Print the failure message and loop continues.


"""
The sum of positive numbers
""" 

def sum_of_positives(my_list):           # Define the function taking a list argument.
    total = 0                            # Initialize a variable to hold the sum.
    for number in my_list:               # Loop through each 'number' in the input list.
        if number > 0:                   # Check if the current number is strictly positive (greater than zero).
            total += number              # If positive, add the number to the running total.
    return total                         # Return the final calculated sum of positive numbers.

if __name__ == "__main__":               # Execute test cases if the script is run directly.
    my_list = [1, -2, 3, -4, 5]          # Sample list containing positive and negative numbers.
    result = sum_of_positives(my_list)   # Call the function.
    print("The result is", result)       # Print the result (should be 1 + 3 + 5 = 9).
    
    my_list_2 = [-10, -5, -1, 0, 10]     # Another sample list.
    result_2 = sum_of_positives(my_list_2) # Call the function.
    print("The result is", result_2)     # Print the result (should be 10).


"""
Even numbers
""" 

def even_numbers(my_list):             # Define the function taking one list argument.
    evens = []                         # Initialize an empty list to store even numbers.
    for number in my_list:             # Loop through each 'number' in the input list.
        if number % 2 == 0:            # Check if the number is divisible by 2 (is even).
            evens.append(number)       # If it's even, add it to the 'evens' list.
    return evens                       # Return the new list containing only even numbers.

if __name__ == "__main__":             # Execute test cases if the script is run directly.
    my_list = [1, 2, 3, 4, 5]          # Sample list.
    new_list = even_numbers(my_list)   # Call the function and store the result.
    
    # Print the original list (to show it's unchanged) and the new list.
    print("original", my_list)         
    print("new", new_list)             # Expected output: [2, 4]
    
    my_list_2 = [10, 11, 12, 13, 14, 15] # Another sample list.
    new_list_2 = even_numbers(my_list_2) # Call the function.
    print("original", my_list_2)
    print("new", new_list_2)           # Expected output: [10, 12, 14]


"""
The sum of lists
""" 

def sum_of_positives(my_list):           # Define the function taking a list argument.
    total = 0                            # Initialize a variable to hold the sum.
    for number in my_list:               # Loop through each 'number' in the input list.
        if number > 0:                   # Check if the current number is strictly positive (> 0).
            total += number              # If positive, add the number to the running total.
    return total                         # Return the final calculated sum.

if __name__ == "__main__":               # Execute test cases if the script is run directly.
    my_list = [1, -2, 3, -4, 5]          # Sample list.
    result = sum_of_positives(my_list)   # Call the function.
    print("The result is", result)       # Print the result (should be 9).
    
    my_list_2 = [-10, -5, -1, 0, 10]     # Another sample list.
    result_2 = sum_of_positives(my_list_2) # Call the function.
    print("The result is", result_2)     # Print the result (should be 10).


"""
Distinct numbers
""" 

def distinct_numbers(my_list):           # Define the function taking a list argument.
    unique_set = set(my_list)            # Convert the list to a set to remove all duplicates.
    sorted_list = sorted(unique_set)     # Convert the set back to a list and sort it.
    return sorted_list                   # Return the new list of unique, sorted numbers.

if __name__ == "__main__":               # Execute test cases if the script is run directly.
    my_list = [3, 2, 2, 1, 3, 3, 1]      # Sample list with duplicates.
    result = distinct_numbers(my_list)   # Call the function.
    print(result)                        # Print the result (should be [1, 2, 3]).
    
    my_list_2 = [10, 5, 10, 5, 1]        # Another sample list.
    result_2 = distinct_numbers(my_list_2) # Call the function.
    print(result_2)                      # Print the result (should be [1, 5, 10]).


"""
The lenght of the longest in the list
""" 

def length_of_longest(my_list):         # Define the function taking a list of strings.
    max_length = 0                      # Initialize the variable to track the maximum length found so far.
    for item in my_list:                # Loop through each 'item' (string) in the input list.
        current_length = len(item)      # Get the length of the current string.
        if current_length > max_length: # Check if the current string is longer than the current maximum.
            max_length = current_length # If it is, update max_length to the current length.
    return max_length                   # Return the final determined maximum length.

if __name__ == "__main__":               # Execute test cases if the script is run directly.
    my_list_1 = ["first", "second", "fourth", "eleventh"] # Sample list 1.
    result_1 = length_of_longest(my_list_1) # Call the function.
    print(result_1)                      # Print the result (should be 8).
    
    my_list_2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"] # Sample list 2.
    result_2 = length_of_longest(my_list_2) # Call the function.
    print(result_2)                      # Print the result (should be 7).


"""
The shortest in the list
""" 

def shortest(my_list):                   # Define the function taking a list of strings.
    shortest_string = my_list[0]         # Initialize the shortest_string with the first element.
    
    # Start iterating from the second element (index 1) since the first is already checked.
    for item in my_list[1:]:             # Loop through all items in the list starting from the second one.
        # Check if the length of the current item is strictly less than the length of the shortest string found so far.
        if len(item) < len(shortest_string): 
            shortest_string = item       # If it is shorter, update shortest_string to this new item.
            
    return shortest_string               # Return the final shortest string found.

if __name__ == "__main__":               # Execute test cases if the script is run directly.
    my_list_1 = ["first", "second", "fourth", "eleventh"] # Sample list 1.
    result_1 = shortest(my_list_1)       # Call the function.
    print(result_1)                      # Print the result (should be "first").
    
    my_list_2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"] # Sample list 2.
    result_2 = shortest(my_list_2)       # Call the function.
    print(result_2)                      # Print the result (should be "tim").


"""
All the longest in the list
""" 

def all_the_longest(my_list):           # Define the function taking a list of strings.
    if not my_list:                     # Check for the edge case of an empty list.
        return []                       # Return an empty list immediately if the input is empty.

    max_len = 0                         # Initialize a variable to track the maximum length.
    for item in my_list:                # First loop: iterate to find the actual maximum length.
        max_len = max(max_len, len(item)) # Update max_len if the current string is longer.

    longest_strings = []                # Initialize an empty list to store the results.
    for item in my_list:                # Second loop: iterate to collect strings of max_len.
        if len(item) == max_len:        # Check if the current string's length matches the maximum.
            longest_strings.append(item)  # If it matches, add the string to the result list.
            
    return longest_strings              # Return the new list containing all the longest strings.

if __name__ == "__main__":               # Execute test cases if the script is run directly.
    my_list_1 = ["first", "second", "fourth", "eleventh"] # Sample list 1.
    result_1 = all_the_longest(my_list_1) # Call the function.
    print(result_1)                      # Print the result (should be ['eleventh']).
    
    my_list_2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"] # Sample list 2.
    result_2 = all_the_longest(my_list_2) # Call the function.
    print(result_2)                      # Print the result (should be ['dorothy', 'richard']).