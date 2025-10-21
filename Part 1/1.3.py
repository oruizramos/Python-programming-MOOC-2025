"""
# https://programming-25.mooc.fi/part-1/3-more-about-variables
"""

"""
# Extra space
"""

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print()
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print()
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

"""
# Arithmetics
"""

x = 27
y = 15

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

"""
# Fix the code: Print a single line
"""

print(5 , end="")
print(" + " , end="")
print(8 , end="")
print(" - " , end="")
print(4 , end="")
print(" = " , end="")
print(5 + 8 - 4 , end="")
