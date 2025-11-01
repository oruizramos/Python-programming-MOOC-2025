"""
https://programming-25.mooc.fi/part-4/6-strings-and-lists
""" 

"""
Everything reversed
""" 

def everything_reversed(my_list):           # Define the function taking a list of strings.
    new_list = []                           # Initialize an empty list for the reversed results.
    
    # Iterate through the original list in reverse order using the reversed() function.
    for item in reversed(my_list):          
        reversed_item = item[::-1]          # Reverse the characters of the current string using slicing.
        new_list.append(reversed_item)      # Add the character-reversed string to the new list.
        
    return new_list                         # Return the new list, which is now doubly reversed.

if __name__ == "__main__":                   # Execute test cases if the script is run directly.
    my_list = ["Hi", "there", "example", "one more"] # Sample list.
    new_list = everything_reversed(my_list) # Call the function.
    print(new_list)                          # Print the result (should be ['erom eno', 'elpmaxe', 'ereht', 'iH']).

"""
Most common character
""" 

def most_common_character(my_string):       # Define function taking one string argument.
    counts = {}                             # Initialize a dictionary to store character frequencies.
    
    for char in my_string:                  # First pass: loop through the string to count characters.
        counts[char] = counts.get(char, 0) + 1 # Increment the count for the current character.
        
    max_count = -1                          # Initialize the maximum count found so far.
    most_common_char = ""                   # Initialize the result character.
    
    # Second pass: iterate through the original string to respect insertion order (tie-breaker).
    for char in my_string:                  
        current_count = counts[char]        # Get the frequency of the current character.
        
        if current_count > max_count:       # Check if the current character's count is strictly greater.
            max_count = current_count       # If so, update the maximum count.
            most_common_char = char         # And update the most common character to this one.
            
    return most_common_char                 # Return the character with the highest frequency (or earliest tie).

if __name__ == "__main__":                   # Execute test cases if the script is run directly.
    first_string = "abcdbde"                # Sample string 1.
    print(most_common_character(first_string)) # Test case for 'b'.
    
    second_string = "exemplaryelementary"   # Sample string 2.
    print(most_common_character(second_string))# Test case for 'e'.

"""
No vowels allowed
""" 

def no_vowels(my_string):                   # Define function taking one string argument.
    vowels = "aeiou"                        # Define a string containing all lowercase vowels.
    new_string = ""                         # Initialize an empty string for the result.
    for char in my_string:                  # Loop through each character in the input string.
        if char not in vowels:              # Check if the current character is NOT a vowel.
            new_string += char              # If it's not a vowel, append it to the new string.
    return new_string                       # Return the resulting string without vowels.

if __name__ == "__main__":                   # Execute test cases if the script is run directly.
    my_string = "this is an example"        # Sample input string.
    print(no_vowels(my_string))             # Call the function and print the result.



"""
No shouting allowed
""" 

def no_shouting(my_list):                       # Define function taking a list of strings.
    new_list = []                               # Initialize an empty list for non-shouting strings.
    for item in my_list:                        # Loop through each string item in the input list.
        if not item.isupper():                  # Check if the item is *NOT* entirely uppercase.
            new_list.append(item)               # If it's not shouting, add the item to the new list.
    return new_list                             # Return the list containing only non-shouting strings.

if __name__ == "__main__":                       # Execute test cases if the script is run directly.
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"] # Sample data.
    pruned_list = no_shouting(my_list)          # Call the function to filter the list.
    print(pruned_list)                          # Print the result.



"""
Neighbours in a list
""" 

def longest_series_of_neighbours(my_list):   # Define function to find the length of the longest neighbour series.
    if not my_list:                         # Check if the input list is empty.
        return 0                            # If empty, the longest series length is 0.

    max_length = 1                          # Initialize maximum length found so far (minimum is 1 for any non-empty list).
    current_length = 1                      # Initialize the length of the current series being checked.
    
    # Iterate through the list starting from the second element (index 1).
    for i in range(1, len(my_list)):        
        prev_item = my_list[i - 1]          # Get the previous item in the list.
        current_item = my_list[i]           # Get the current item in the list.
        
        # Check if the absolute difference between the current and previous item is exactly 1.
        if abs(current_item - prev_item) == 1: 
            current_length += 1             # If they are neighbours, increment the current series length.
        else:                               # If they are not neighbours (the series is broken).
            current_length = 1              # Reset the current series length back to 1 (for the new item).
            
        # After checking the link, update the overall maximum length found.
        if current_length > max_length:     
            max_length = current_length     # Store the new maximum length if the current streak is longer.
            
    return max_length                       # Return the final maximum length found.

if __name__ == "__main__":                   # Execute test cases if the script is run directly.
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0] # Sample list 1.
    print(longest_series_of_neighbours(my_list)) # Expected output: 4.

    my_list_2 = [1, 2, 3, 2, 1, 0, 1]       # Sample list 2 for further testing.
    print(longest_series_of_neighbours(my_list_2)) # Expected output: 6.



"""
Grade statistics
""" 

results = []                                # Initialize an empty list to store all valid student result tuples (exam, exercises).
grade_counts = [0] * 6                      # Initialize a list to count grades (index 0 for fail, 1-5 for passing grades).
passing_count = 0                           # Initialize a counter for students who passed (grade >= 1).
total_points = 0                            # Initialize accumulator for total (exam + exercise) points.
total_submissions = 0                       # Initialize counter for total number of student submissions.

while True:                                 # Start an infinite loop to collect input.
    # Prompt the user for input and store the whole line as a string.
    line = input("Exam points and exercises completed: ")
    
    if line == "":                          # Check if the line is empty (the exit condition).
        break                               # Exit the while loop if the line is empty.
        
    parts = line.split()                    # Split the line into a list of strings (exam points and exercises).
    exam_points = int(parts[0])             # Convert the first part to an integer (exam points).
    exercises = int(parts[1])               # Convert the second part to an integer (exercises completed).

    # --- Calculation Logic ---

    # Calculate exercise points: 10% of exercises completed grants 1 point, rounded down.
    exercise_points = exercises // 10       
    
    final_points = exam_points + exercise_points # Calculate total points.
    
    # --- Grading Logic ---
    
    grade = 0                               # Default grade is 0 (fail).
    
    # Apply exam cutoff threshold: Automatic fail if exam points are less than 10.
    if exam_points < 10:
        grade = 0
    # Apply grading scale based on total points.
    elif 15 <= final_points <= 17:
        grade = 1
    elif 18 <= final_points <= 20:
        grade = 2
    elif 21 <= final_points <= 23:
        grade = 3
    elif 24 <= final_points <= 27:
        grade = 4
    elif final_points >= 28:
        grade = 5
        
    # --- Statistics Accumulation ---
    
    # Accumulate data for statistics report.
    grade_counts[grade] += 1                # Increment the count for the determined grade.
    total_points += final_points            # Add total points to the overall sum.
    total_submissions += 1                  # Increment the submission count.
    
    if grade >= 1:                          # Check if the student passed (grade 1 or higher).
        passing_count += 1                  # Increment the pass count.

# --- Statistics Output ---

print("Statistics:")                        # Print the header for the statistics section.

# Calculate average points. Avoid division by zero if no submissions were made.
if total_submissions > 0:                   
    points_avg = total_points / total_submissions # Calculate the average points.
    pass_perc = (passing_count / total_submissions) * 100 # Calculate the pass percentage.
else:
    points_avg = 0.0                        # Default to 0.0 if no submissions.
    pass_perc = 0.0                         # Default to 0.0 if no submissions.

# Print points average, formatted to one decimal place.
print(f"Points average: {points_avg:.1f}")  

# Print pass percentage, formatted to one decimal place.
print(f"Pass percentage: {pass_perc:.1f}")

print("Grade distribution:")                # Print the header for grade distribution.

# Print the distribution from grade 5 down to 0.
for i in range(5, -1, -1):                  # Loop backwards from 5 to 0 (inclusive).
    stars = "*" * grade_counts[i]           # Create a string of stars equal to the count for the grade.
    print(f"  {i}: {stars}")                # Print the grade number followed by the star distribution.