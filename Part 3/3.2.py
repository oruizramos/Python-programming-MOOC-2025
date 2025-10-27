"""
# https://programming-25.mooc.fi/part-3/2-working-with-strings
"""

#Developer manthra “Make it work → Make it clear → Make it clean → Make it scalable.” In that order

#| Priority | Focus                                                       |
#| -------- | ----------------------------------------------------------- |
#| 🥇 1     | **Correctness** – does it do what it’s supposed to?         |
#| 🥈 2     | **Clarity** – can you or someone else read it easily later? |
#| 🥉 3     | **Maintainability** – can it be extended cleanly?           |
#| 🏁 4     | **Optimization** – can it run faster or use less code?      |


"""
# String multiplied
"""

word = input("Please type in a string: ")
times = int(input("Please type in an amount: "))

print(word * times)


"""
# The longer string
"""

string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string2) > len(string1):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")

"""
# End to beginning
"""

string = input("Please type in a string: ")
index = len(string) - 1 #For reverse order, it must be initialized at the end of the last possible index -1

while index >= 0:
    print(string[index])
    index -= 1 #Since index was initialized at the end, we most traverse backwards -1

#KEY TAKEAWAYS:
#For standard order: index = 0
#For reverse order: index = len(string) - 1

"""
# Second and second to last characters
"""

string = input("Please type in a string: ")
second_index = string[1]
second_to_last_index = string[-2]

if len(string) > 1:  #Condition to check that the word is at least 2 characters long
    if second_index == second_to_last_index:
        print(f"The second and the second to last characters are {second_index}")
    else:
        print("The second and the second to last characters are different")


"""
# A line of hashes
"""

width = int(input("Width: "))
character = "#"

print(f"{character}" * width)


"""
# A rectangle of hashes
"""

# Rule of thump: “If you don’t have a special reason to count down, count up.”

width = int(input("Width: "))
height = int(input("Height: "))
character = "#"

n = 0
while n < height:
    print(character * width)
    n += 1

# I originally had the following version, but apparently due to the previous rule of thumb, it was a bad practice. It also:
#The loop destroys the value of n (it ends up 0).
#If ever the need to use height again inside the loop (e.g., to label rows), another variable would be needed anyway.

#width = int(input("Width: "))
#height = int(input("Height: "))
#character = "#"

#n = height
#while n > 0:
    #print(character * width)
    #n -= 1

"""
# Underlining
"""

# “Sentinel-controlled loop” pattern.This order follows the classic “Input → Check → Process” flow

character = "-"

while True:
    string = input("Please type in a string: ")  #1. Input
    if string == "":                             #2. Check for exit/Break
        break
    print(string)                                #3. Output 
    print(len(string) * character)
    


"""
# Right-aligned
"""
string = input("Please type in a string: ")
character = "*"
full_lenght = 20 - len(string)

print((full_lenght * character) + string)

# ================= Calculations (Split vs Combine) =================
#
# Example: Formatting a string to 20 chars with '*' padding
# 
# --------Rule of thumb for Python beginners----------
# Ask yourself: “Would someone reading this for the first time immediately understand what’s happening?”
# If yes → combining is okay.
# If no → split into meaningful variables with clear names.
#
# ---------------- Split calculation ----------------
# string = "python"
# padding = 20 - len(string)       # calculate number of '*' separately
# stars   = "*" * padding          # build the padding string
# formatted_string = stars + string
# print(formatted_string)
#
# Advantages:
# - Each step is clear and named
# - Easy to debug intermediate values
# - Easier to modify or extend later
#
# ---------------- Combine calculation ----------------
# string = "python"
# formatted_string = "*" * (20 - len(string)) + string
# print(formatted_string)
#
# Advantages:
# - Shorter
# - Works for simple cases
#
# Disadvantages:
# - Harder to read if expression is complex
# - No intermediate values to debug
#
# Rule of Thumb:
# - Split for clarity and maintainability
# - Combine for short, obvious expressions
#
# =====================================================

"""
# A framed word
"""

word = input("Word: ")
frame_width = 30
character = "*"

# Calculate available space for padding (excluding the border characters)
space = frame_width - 2 - len(word)
left_padding  = space // 2
right_padding = space - left_padding

# Middle line creation with f string concatenation. 
middle_line = f"{character}{' ' * left_padding}{word}{' ' * right_padding}{character}"

print(character * frame_width)
print(middle_line)
print(character * frame_width)

#Key takeaway:
#Multiplying a string by an integer always gives a string. Concatenating only works with strings. F-strings automatically handle conversion, so they are safer and cleaner.

"""
# Substrings, part 1
"""

string = input("Please type in a string: ")
second_slice = 1

while second_slice <= len(string):
    #Half-open intervals: string[start:end] = includes the start index, but excludes the end index. 
    print(string[0:second_slice]) #Even if when the first print is [0,1], it only prints the start of the index. 
    second_slice += 1

"""
# Substrings, part 2
"""

string = input("Please type in a string: ")
first_slice = len(string) - 1   #len(string) - 1 Standard notation to start at the end of a string

while first_slice >= 0:
    #Half-open intervals: string[start:end] = includes the start index, but excludes the end index. 
    print(string[first_slice:]) #Now the first print is [lastindex,], so it prints the slices backwards
    first_slice -= 1

"""
# Does it contain vowels
"""

string = input("Please type in a string: ")
vowels = "aeo" #Store all vowels at once to loop over them instead of writing a separate if for "a", "e", and "o".
index = 0 #Tracker to "move" through each vowel.

while index < len(vowels): #Loop goes through each vowel one by one.
    vowel = vowels[index] #The same if vowel in string: block can work for "a", "e", "o" automatically
    #In python, if a condition already returns a True/False value,👉 never add == True or == False.
    if vowel in string: #This will return either True or False already
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1

"""
# Find the first substring
"""

word = input("Please type in a word: ")
character = input("Please type in a character: ")

# Find the index of the first occurrence of the character in the word
index = word.find(character)
# Check if the character was found AND if there are at least 3 characters remaining starting from that index
# - index != -1 makes intention clearer: “if character was found.”
# - len(word) - index >= 3 ensures slicing three characters won't go out of bounds
if index != -1 and len(word) - index >= 3:  
    print(word[index:index + 3])

#No need to print else, since the nothings needs to be printed/done in any other case

"""
# Find all the substrings
"""

word = input("Please type in a word: ")
character = input("Please type in a character: ")

while True:
    #Defining index inside the loop ensures the search is always relative to the current string.
    #If defined outside, it would only work for the original string and fail as soon as word is updated.
    #Iteratively processing a shrinking or changing collection: recalculate the “position” each time.
    index = word.find(character) 
    if index != -1 and len(word) - index >= 3:
        print(word[index:index + 3])
        word = word[index + 1:]
    else:
        break
        
    
"""
# The second occurence 
"""

# Step 1: Get input
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

# Step 2: Find the first occurrence
first_index = string.find(substring)

# Step 3: Check if it exists at all
if first_index == -1:
    print("The substring does not occur twice in the string.")
else:
    # Step 4: Find the second occurrence
    second_index = string.find(substring, first_index + len(substring))
    
    # Step 5: Check if the second occurrence exists
    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
