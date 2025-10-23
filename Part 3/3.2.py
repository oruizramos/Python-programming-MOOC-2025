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