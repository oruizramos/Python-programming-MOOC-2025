"""
# https://programming-25.mooc.fi/part-6/2-writing-files
""" 

"""
# Inscription
""" 

name = input("Whom should I sign this to: ")

filename = input("Where shall I save it: ")

inscription = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"

# 4. Write the inscription to the specified file
# Using 'with open' ensures the file is automatically closed, even if errors occur.
try:
    with open(filename, "w") as file:
        file.write(inscription)
except IOError as e:
    # Print an error message if the file cannot be written (e.g., permission denied)
    print(f"Error writing to file {filename}: {e}")

# The program finishes without printing any further output, just like the example.


"""
# Diary
""" 

# The name of the file used to store diary entries
FILENAME = "diary.txt"

# Start the main program loop
while True:
    # Display the menu options
    print("1 - add an entry, 2 - read entries, 0 - quit")
    
    # Get the user's choice
    choice = input("Function: ")

    if choice == "1":
        # OPTION 1: Add a new entry
        entry = input("Diary entry: ")
        
        # Open the file in append mode ('a') to add the new entry to the end
        with open(FILENAME, "a") as file:
            # Write the entry followed by a newline character
            file.write(entry + "\n")
            
        print("Diary saved")

    elif choice == "2":
        # OPTION 2: Read and display all entries
        print("Entries:")
        
        # Use a try-except block to handle the case where the file hasn't been created yet
        try:
            # Open the file in read mode ('r')
            with open(FILENAME, "r") as file:
                # Read the entire content of the file
                content = file.read()
                # Print the content. The 'end=""' prevents an extra newline 
                # because the entries already include one.
                print(content, end="")
        except FileNotFoundError:
            # Do nothing if the file doesn't exist (i.e., no entries yet)
            pass

    elif choice == "0":
        # OPTION 0: Quit the program
        print("Bye now!")
        break
    
    # If the choice is anything else, the loop simply restarts, asking for input again.


"""
# Filtering the contents of a file
""" 

"""
# Store personal data
""" 

"""
# Course grading, part 4
""" 

"""
# Word search
""" 

"""
# Dictionary stored in a file
""" 