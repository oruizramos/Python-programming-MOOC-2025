"""
https://programming-25.mooc.fi/part-4/3-lists
""" 

"""
Change the value of an item
""" 

my_list = [1, 2, 3, 4, 5]                  # Initialize the list with the required starting values.

while True:                                # Start an infinite loop to continuously ask for input.
    index_input = input("Index: ")         # Prompt the user to type in an index.
    index = int(index_input)               # Convert the user's index input from string to integer.
    
    if index == -1:                        # Check the exit condition specified in the problem.
        break                              # If index is -1, break out of the infinite loop.
        
    value_input = input("New value: ")     # Prompt the user for the new value to be inserted.
    new_value = int(value_input)           # Convert the new value input from string to integer.
    
    my_list[index] = new_value             # Replace the value at the specified index with the new value.
    
    print(my_list)                         # Print the updated list to show the result of the change.

print("Bye!")                              # Print a farewell message after the loop breaks (optional, but good practice).

"""
Add items to a list
""" 

# Get the total number of items from the user.
count_input = input("How many items: ")        # Prompt the user for the count.
count = int(count_input)                       # Convert the input string to an integer.

my_list = []                                   # Initialize an empty list to store the items.

# Loop for the specified number of times (from 0 up to count - 1).
for i in range(count):                         # The loop runs 'count' times.
    # Calculate the current item number for the prompt (starting at 1).
    item_number = i + 1                        # Use 'i + 1' for display purposes (e.g., "Item 1").
    
    # Construct the dynamic prompt string.
    prompt = f"Item {item_number}: "           # Create the prompt string, e.g., "Item 1: ".
    
    # Get the item value from the user.
    item_value = input(prompt)                 # Prompt the user and read the input value.
    
    # Convert the value to an integer before adding it to the list.
    # Note: If the problem required strings, this line would be different or omitted.
    new_item = int(item_value)                 # Convert the item input to an integer.
    
    my_list.append(new_item)                   # Add the converted integer value to the end of the list.

print(my_list)                                 # Print the final list containing all collected items.


"""
Addition and removal
""" 

my_list = []                                   # Initialize an empty list as the starting point.

while True:                                    # Start an infinite loop to run the program until the user exits.
    print(f"The list is now {my_list}")        # Print the current state of the list before asking for the next command.
    
    # Prompt the user for the next action.
    choice = input("a(d)d, (r)emove or e(x)it: ") # Get the user's command (d, r, or x).
    
    if choice == "d":                          # Check if the user chose to add an item.
        if len(my_list) == 0:                  # Check if the list is currently empty.
            new_item = 1                       # If empty, the first item added must be 1.
        else:                                  # If the list is not empty:
            last_item = my_list[-1]            # Get the value of the last item in the list.
            new_item = last_item + 1           # The new item is one greater than the last item.
        
        my_list.append(new_item)               # Add the calculated new item to the end of the list.
        
    elif choice == "r":                        # Check if the user chose to remove an item.
        if len(my_list) > 0:                   # Check if the list is non-empty before attempting removal.
            my_list.pop()                      # Remove and discard the last item from the list.
        # Note: We rely on the assumption that removal won't be attempted on an empty list.
        
    elif choice == "x":                        # Check if the user chose to exit the program.
        break                                  # Exit the 'while True' loop.

print("Bye!")                                  # Print a farewell message after the loop has been broken.


"""
Same words twice
""" 

words_typed = []                               # Initialize an empty list to track all unique words entered.

while True:                                    # Start an infinite loop to repeatedly ask for input.
    word = input("Word: ")                     # Prompt the user for a word.
    
    if word in words_typed:                    # Check if the currently entered word is already in the list.
        # The word has been typed for the second time, so the program must calculate and exit.
        
        # Convert the list to a set to automatically filter out duplicates.
        unique_words = set(words_typed)        # A set contains only unique elements.
        
        # The number of different words is the length of the set.
        count = len(unique_words)              # Get the total count of unique words.
        
        # Print the required final output message.
        print(f"You typed in {count} different words") # Output the result based on the unique count.
        break                                  # Exit the 'while True' loop to end the program.
        
    else:                                      # If the word is being typed for the first time:
        words_typed.append(word)               # Add the new word to the list for future checks.


"""
List twice
""" 
my_list = []                                   # Initialize an empty list to store the user's values.

while True:                                    # Start an infinite loop to repeatedly ask for input.
    # Prompt the user for a new item.
    new_item_input = input("New item: ")       # Get the user's input as a string.
    
    # Convert the input string to an integer.
    # Note: A real-world application would use try/except for error handling here.
    new_item = int(new_item_input)             # Convert the input to an integer.
    
    if new_item == 0:                          # Check the exit condition: if the user typed 0.
        break                                  # Exit the 'while True' loop.
    
    # If the user did not type 0, proceed with processing the item.
    my_list.append(new_item)                   # Add the new integer value to the end of the list.
    
    # --- Output 1: List in the order items were added (original order) ---
    print(f"The list now: {my_list}")          # Print the list as it currently exists.
    
    # --- Output 2: List ordered from smallest to greatest (sorted order) ---
    # Create a *new*, sorted copy of the list for printing.
    # We use sorted() so the original 'my_list' remains in insertion order.
    sorted_list = sorted(my_list)              # Create a new list containing the elements sorted numerically.
    print(f"The list in order: {sorted_list}") # Print the newly created sorted list.

print("Bye!")                                  # Print a farewell message after the loop has ended.


"""
The lenght of a list
""" 
def length(my_list):                             # Define a function named 'length' that accepts one argument, 'my_list'.
    return len(my_list)                         # Use the built-in Python function 'len()' to calculate and return the list's length.

# Testing the function:
if __name__ == "__main__":                      # Standard Python entry point for running test code directly.
    my_list = [1, 2, 3, 4, 5]                  # Initialize a list with five elements for testing.
    result = length(my_list)                   # Call the function with the list and store the result.
    print("The length is", result)             # Print the result of the function call (should be 5).
                                                # Add a blank line for separation in the output.
    # Test case where the list is passed directly without assigning it to a variable.
    result = length([1, 1, 1, 1])              # Call the function directly with a temporary list.
    print("The length is", result)             # Print the result of the second function call (should be 4).


"""
Arithmetic mean
""" 
def mean(my_list):                               # Define a function named 'mean' that accepts a list of numbers.
    list_sum = sum(my_list)                      # Calculate the sum of all elements in the list using the built-in 'sum()'.
    list_length = len(my_list)                   # Get the count of elements using the built-in 'len()'.

    if list_length == 0:                         # Check if the list is empty to prevent division by zero.
        return 0.0                               # Return 0.0 if the list is empty (or handle as required).

    return list_sum / list_length                # Calculate and return the mean (sum divided by count).

# Testing the function:
if __name__ == "__main__":                      # Standard Python entry point for running test code directly.
    my_list = [1, 2, 3, 4, 5]                  # Initialize a sample list for testing.
    result = mean(my_list)                     # Call the mean function and store the result.
    print("mean value is", result)             # Print the calculated mean value (should be 3.0).

    # Additional test case:
    print("mean value is", mean([10, 20]))     # Test the function by passing a list directly (should be 15.0).


"""
The range of a list
""" 

def range_of_list(my_list):                      # Define a function named 'range_of_list' that takes a list.
    if not my_list:                              # Check if the list is empty to handle edge cases.
        return 0                                 # If the list is empty, the range is 0.
    
    largest_value = max(my_list)                 # Find the largest value in the list using the built-in max().
    smallest_value = min(my_list)                # Find the smallest value in the list using the built-in min().
    
    return largest_value - smallest_value        # Return the difference between the largest and smallest values.

# Testing the function:
if __name__ == "__main__":                      # Standard Python entry point for running test code directly.
    my_list = [1, 2, 3, 4, 5]                  # Initialize a sample list for testing.
    result = range_of_list(my_list)            # Call the function and store the returned range.
    print("The range of the list is", result)  # Print the result (should be 4).

    # Additional test case:
    result = range_of_list([10, -5, 20])       # Test with different numbers and a direct list argument.
    print("The range of the list is", result)  # Print the result (should be 25).

