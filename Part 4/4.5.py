"""
https://programming-25.mooc.fi/part-4/5-print-statement-formatting
""" 

"""
Integers to strings
""" 

def formatted(my_list):                 # Define the function taking a list of floats.
    new_list = []                       # Initialize an empty list to store the formatted strings.
    for number in my_list:              # Loop through each floating point number in the input list.
        # Use an f-string to format the number as a string, rounded to two decimal places.
        formatted_str = f"{number:.2f}" 
        new_list.append(formatted_str)  # Add the resulting formatted string to the new list.
    return new_list                     # Return the new list of formatted strings.

if __name__ == "__main__":               # Execute test cases if the script is run directly.
    my_list = [1.234, 0.3333, 0.11111, 3.446] # Sample list of floats.
    new_list = formatted(my_list)       # Call the function to get the formatted list.
    print(new_list)                      # Print the result.
