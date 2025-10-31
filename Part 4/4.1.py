"""
# https://programming-25.mooc.fi/part-4/1-vscode
""" 

"""
# Hello Visual Studio Code
""" 


while True:                                             # Start an infinite loop that continues until explicitly broken.
    editor_input = input("Editor: ")                    # Prompt the user to type in the name of their editor and store the input.
    
    # Convert the input to lowercase for case-insensitive comparison
    editor = editor_input.lower()                       # Convert the user's input string entirely to lowercase.
    
    # Check the required conditions
    if editor == "visual studio code":                  # Check if the lowercase input exactly matches the target "visual studio code".
        print("an excellent choice!")                   # Print the success message.
        break                                           # Exit the infinite while loop, ending the program execution.
    elif editor == "word" or editor == "notepad":       # Check if the lowercase input matches "word" OR "notepad".
        print("awful")                                  # Print the specific negative response.
    else:                                               # If none of the specific conditions above were met.
        print("not good")                               # Print the general negative response.