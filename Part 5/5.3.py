"""
# https://programming-25.mooc.fi/part-5/3-dictionary
""" 

"""
# Times ten
""" 
def times_ten(start_index: int, end_index: int) -> dict:
    """
    Creates a new dictionary where keys are integers from start_index 
    to end_index (inclusive), and the values are the keys multiplied by ten.

    Args:
        start_index: The starting integer for the keys (inclusive).
        end_index: The ending integer for the keys (inclusive).

    Returns:
        A dictionary mapping the numbers in the range to their value times ten.
    """
    
    # We use a dictionary comprehension for concise and efficient creation.
    # The range function needs to go up to end_index + 1 to include end_index.
    new_dictionary = {
        i: i * 10 
        for i in range(start_index, end_index + 1)
    }
    
    return new_dictionary

# Example execution:
d = times_ten(3, 6)
print(d)

# Another example:
d2 = times_ten(10, 12)
print(d2)


"""
# Factorials
""" 

def factorials(n: int) -> dict:
    """
    Calculates the factorials for all numbers from 1 up to n and returns 
    them in a dictionary.

    Args:
        n: The upper limit (inclusive) for which to calculate factorials.

    Returns:
        A dictionary where keys are numbers (1 to n) and values are 
        their respective factorials.
    """
    
    # Initialize the dictionary to store the results
    result_dict = {}
    
    # Initialize the current factorial value. 1! is 1.
    current_factorial = 1
    
    # Iterate from 1 up to n (inclusive)
    for i in range(1, n + 1):
        # Calculate the factorial for the current number (i).
        # For i=1, 1 * 1 = 1.
        # For i=2, 2 * 1! = 2.
        # For i=3, 3 * 2! = 6, and so on.
        current_factorial *= i
        
        # Store the number (i) as the key and the calculated factorial as the value
        result_dict[i] = current_factorial
        
    return result_dict

# Example execution:
k = factorials(5)
print(f"Full dictionary: {k}")

# Sample output validation:
print(f"\nFactorial of 1: {k[1]}")
print(f"Factorial of 3: {k[3]}")
print(f"Factorial of 5: {k[5]}")

# Another example:
k_small = factorials(3)
print(f"\nFactorials up to 3: {k_small}")


"""
# Histogram
""" 

def histogram(text: str):
    """
    Calculates the frequency of each letter in a string and prints a 
    histogram where the count is represented by asterisks (*).
    
    Args:
        text: The input string to analyze.
    """
    
    # 1. Initialize a dictionary to store the counts
    letter_counts = {}
    
    # 2. Iterate through the input text to count frequencies
    for char in text:
        # Normalize the character to lowercase to ensure case-insensitivity
        char = char.lower()
        
        # Only process characters that are letters, skipping spaces, punctuation, etc.
        if 'a' <= char <= 'z':
            # Use .get() to safely increment the count, initializing it to 0 if 
            # the letter is seen for the first time.
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
    # 3. Print the histogram
    # Sort the items by letter (key) for consistent output order
    print("--- Histogram ---")
    for letter, count in sorted(letter_counts.items()):
        # Create the string of asterisks
        stars = '*' * count
        
        # Print the letter, a space, and the sequence of stars
        print(f"{letter} {stars}")
    print("-----------------")


# Example executions:
print("Test 1: 'abba'")
histogram("abba")

print("\nTest 2: 'statistically'")
histogram("statistically")

print("\nTest 3: 'Hello World! (Case-insensitive)'")
histogram("Hello World! (Case-insensitive)")


"""
# Phone book, version 1
""" 
# Initialize the phone book as an empty dictionary.
# Keys will be names (str) and values will be numbers (str).
phone_book = {}

print("Welcome to the Phone Book Application")

# Start the main command loop
while True:
    # Prompt the user for the command
    command = input("command (1 search, 2 add, 3 quit): ")

    if command == "2":
        # --- ADD ENTRY ---
        name = input("name: ")
        number = input("number: ")
        
        # Add the entry or update the existing one
        phone_book[name] = number
        print("ok!")

    elif command == "1":
        # --- SEARCH ENTRY ---
        name = input("name: ")
        
        # Check if the name exists in the phone book
        if name in phone_book:
            # If found, print the number
            print(phone_book[name])
        else:
            # If not found, print the "no number" message
            print("no number")
            
    elif command == "3":
        # --- QUIT ---
        print("quitting...")
        break # Exit the while loop

    else:
        # Handle invalid input
        print(f"Invalid command '{command}'. Please use 1, 2, or 3.")


"""
# Phone book, version 2
""" 

# Initialize the phone book as an empty dictionary.
# Keys are names (str), and values are lists of numbers (list[str]).
phone_book = {}

print("Welcome to the Improved Phone Book Application")

# Start the main command loop
while True:
    # Prompt the user for the command
    command = input("command (1 search, 2 add, 3 quit): ")

    if command == "2":
        # --- ADD ENTRY ---
        name = input("name: ")
        number = input("number: ")
        
        # Check if the name already exists in the phone book
        if name in phone_book:
            # If the name exists, append the new number to the existing list
            phone_book[name].append(number)
        else:
            # If the name is new, create a new list containing the single number
            phone_book[name] = [number]
            
        print("ok!")

    elif command == "1":
        # --- SEARCH ENTRY ---
        name = input("name: ")
        
        # Check if the name exists in the phone book
        if name in phone_book:
            # If found, retrieve the list of numbers
            numbers = phone_book[name]
            # Print each number on a new line
            for num in numbers:
                print(num)
        else:
            # If not found, print the "no number" message
            print("no number")
            
    elif command == "3":
        # --- QUIT ---
        print("quitting...")
        break # Exit the while loop

    else:
        # Handle invalid input
        print(f"Invalid command '{command}'. Please use 1, 2, or 3.")


"""
# Invert a dictionary
""" 
def invert(dictionary: dict):
    # 1. Capture the original items. This is crucial because we cannot iterate
    # over a dictionary while simultaneously modifying its structure (e.g., clearing it).
    original_items = list(dictionary.items())

    # 2. Clear the original dictionary to perform the "in-place" inversion.
    dictionary.clear()

    # 3. Repopulate the dictionary with inverted keys (old values) and values (old keys).
    for key, value in original_items:
        # The value becomes the new key, and the key becomes the new value.
        dictionary[value] = key

# Example usage as requested:
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)
# Expected output: {"first": 1, "second": 2, "third": 3, "fourth": 4}

s2 = {"a": 10, "b": 20, "c": 30}
invert(s2)
print(s2)
# Expected output: {10: "a", 20: "b", 30: "c"}

"""
# Numbers spelled out
""" 

def dict_of_numbers() -> dict:
    """
    Returns a dictionary mapping numbers 0-99 to their spelled-out word forms.
    The dictionary is built using helper dictionaries and loops to avoid
    hardcoding all 100 entries.
    """
    
    # Helper Dictionaries for the building blocks
    SINGLES = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    TEENS = {
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    # Keys are the tens digits (e.g., 2 for twenty, 9 for ninety)
    TENS = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"
    }
    
    # Initialize the final result dictionary
    numbers = {}

    # 1. Populate 0-9 (Singles)
    for i in range(10):
        numbers[i] = SINGLES[i]

    # 2. Populate 10-19 (Teens - irregular structure)
    for i in range(10, 20):
        numbers[i] = TEENS[i]

    # 3. Populate 20-99 (Tens and Composites)
    for i in range(20, 100):
        # Calculate the tens digit (2, 3, 4, ... 9) and the ones digit (0-9)
        tens_digit = i // 10
        ones_digit = i % 10

        tens_word = TENS[tens_digit]

        if ones_digit == 0:
            # If the ones digit is 0 (e.g., 20, 30, 40), we use the tens word only
            numbers[i] = tens_word
        else:
            # For composite numbers (e.g., 45), combine the tens word, a hyphen,
            # and the singles word.
            ones_word = SINGLES[ones_digit]
            numbers[i] = f"{tens_word}-{ones_word}"

    return numbers

# Example Usage:
numbers = dict_of_numbers()

print(f"2: {numbers[2]}")
print(f"11: {numbers[11]}")
print(f"45: {numbers[45]}")
print(f"99: {numbers[99]}")
print(f"0: {numbers[0]}")

"""
# Movie database
""" 
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    """
    Adds a new movie dictionary to the provided database list.

    Args:
        database (list): The list where movie dictionaries are stored.
        name (str): The name of the movie.
        director (str): The director of the movie.
        year (int): The release year of the movie.
        runtime (int): The runtime of the movie in minutes.
    """
    # Create the dictionary object using the function arguments
    new_movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }

    # Append the new movie dictionary to the database list
    database.append(new_movie)

# Example Usage:
database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)

# Print the resulting database list
print(database)


"""
# Find movies
""" 
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    """
    Adds a new movie dictionary to the provided database list.
    (Included from the previous problem for a runnable example).
    """
    new_movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(new_movie)

def find_movies(database: list, search_term: str) -> list:
    """
    Filters the movie database, returning a new list containing only 
    movies whose title includes the search term, ignoring case.

    Args:
        database (list): The list of movie dictionaries.
        search_term (str): The term to search for within movie names.

    Returns:
        list: A new list of movie dictionaries matching the search term.
    """
    matching_movies = []
    
    # Convert the search term to lowercase once for efficiency
    normalized_search = search_term.lower()

    for movie in database:
        # Get the movie name and convert it to lowercase for case-insensitive comparison
        movie_name = movie["name"].lower()
        
        # Check if the normalized search term is a substring of the normalized movie name
        if normalized_search in movie_name:
            matching_movies.append(movie)

    return matching_movies

# Example Usage:
database = []
# Populate the database using the helper function
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
add_movie(database, "Dawn of the Dead Programmers", "M. Night Python", 2011, 101)

# Search for "python" (case-insensitive)
my_movies = find_movies(database, "python")
print(my_movies)

# Search for a different term, like "plane"
plane_movies = find_movies(database, "Plane")
print("\nSearch for 'Plane':")
print(plane_movies)