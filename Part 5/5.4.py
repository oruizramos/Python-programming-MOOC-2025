"""
# https://programming-25.mooc.fi/part-5/4-tuple
""" 

"""
# Create a tuple
""" 
def create_tuple(x: int, y: int, z: int) -> tuple:
    """
    Takes three integers and returns a tuple containing:
    (smallest_argument, greatest_argument, sum_of_arguments).

    Args:
        x (int): The first integer.
        y (int): The second integer.
        z (int): The third integer.

    Returns:
        tuple: A tuple containing the smallest, greatest, and sum of the three inputs.
    """
    # 1. Find the smallest value
    smallest = min(x, y, z)

    # 2. Find the greatest value
    greatest = max(x, y, z)

    # 3. Calculate the sum
    total_sum = x + y + z

    # Return the new tuple in the specified order
    return (smallest, greatest, total_sum)

if __name__ == "__main__":
    # Example usage: 5, 3, -1 -> min is -1, max is 5, sum is 7
    print(create_tuple(5, 3, -1))

    # Another test case
    print(create_tuple(10, 2, 5))


"""
# The oldest person
""" 
def oldest_person(people: list) -> str:
    """
    Finds the oldest person from a list of (name, year_of_birth) tuples.
    The oldest person has the smallest year of birth.

    Args:
        people (list): A list of tuples, e.g., [("Name", 1990), ("Other", 1950)]

    Returns:
        str: The name of the oldest person.
    """
    # Use the min function to find the tuple with the minimum value at index 1 (the year).
    # The result will be the tuple (name, year) of the oldest person.
    oldest_person_tuple = min(people, key=lambda person: person[1])

    # Return the name, which is the element at index 0 of the resulting tuple.
    return oldest_person_tuple[0]

# Example of the function in action:
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    
    print(f"The oldest person is: {oldest_person(people)}")
    
    # Test case with same oldest year
    p5 = ("Bob", 1953)
    people_2 = [p1, p2, p3, p4, p5]
    print(f"Test with tie (Mary is first): {oldest_person(people_2)}")

"""
# Older people
"""
from typing import List, Tuple

def older_people(people: List[Tuple[str, int]], year: int) -> List[str]:
    """
    Selects the names of all people who were born before the given year.

    Args:
        people (list): A list of (name, year_of_birth) tuples.
        year (int): The cutoff year. People born before this year are included.

    Returns:
        list: A list containing the names of the older people.
    """
    # Use a list comprehension to filter the people list
    # For each (name, birth_year) tuple:
    # 1. Check the condition: if birth_year < year
    # 2. If true, include the name in the new list
    older_names = [name for name, birth_year in people if birth_year < year]

    return older_names

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)

    # Test case 2: Born before 1990
    older_than_1990 = older_people(people, 1990)
    print(f"Born before 1990: {older_than_1990}")

"""
# Student database
""" 

from typing import List, Tuple, Dict, Any

# The database structure will be:
# students = {
#     "Student Name": {
#         "courses": {
#             "Course Name": Grade,
#             ...
#         }
#     },
#     ...
# }

def add_student(students: Dict[str, Any], name: str):
    """
    Adds a new student to the database, initializing their courses dictionary.
    """
    # Initialize the student's entry with an empty dictionary for courses
    if name not in students:
        students[name] = {"courses": {}}

def add_course(students: Dict[str, Any], name: str, course_data: Tuple[str, int]):
    """
    Adds a completed course to a student's record, handling repetition and grade 0.
    - Grade 0 courses are ignored.
    - If a course is repeated, only the higher grade is recorded.
    """
    if name not in students:
        print(f"Error: Student '{name}' not found.")
        return

    course_name, new_grade = course_data
    
    # 1. Ignore courses with grade 0
    if new_grade <= 0:
        return

    student_courses = students[name]["courses"]
    
    # Get the existing grade, or 0 if the course hasn't been taken yet
    existing_grade = student_courses.get(course_name, 0)

    # 2. Only record the new grade if it's higher than the existing one
    if new_grade > existing_grade:
        student_courses[course_name] = new_grade

def print_student(students: Dict[str, Any], name: str):
    """
    Prints the information for a single student: course count, course list, and average grade.
    """
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    student_courses = students[name]["courses"]
    course_count = len(student_courses)

    if course_count == 0:
        print(f"{name}:\n no completed courses")
        return

    # Calculate average grade
    total_grade_sum = sum(student_courses.values())
    average_grade = float(total_grade_sum) / course_count

    print(f"{name}:")
    print(f" {course_count} completed courses:")
    
    # Print the list of courses, sorted by course name for clean output
    for course, grade in sorted(student_courses.items()):
        print(f"  {course} {grade}")
        
    # Format average grade to one decimal place
    print(f" average grade {average_grade:.1f}")

def summary(students: Dict[str, Any]):
    """
    Prints a summary of the entire database: total students, student with most courses,
    and student with the best average grade.
    """
    print(f"students {len(students)}")
    
    if not students:
        return

    max_courses = -1
    most_courses_student = ""
    best_avg = -1.0
    best_avg_student = ""
    
    for name, data in students.items():
        courses = data["courses"]
        course_count = len(courses)
        
        # 1. Check for most courses completed
        if course_count > max_courses:
            max_courses = course_count
            most_courses_student = name
            
        # 2. Check for best average grade (only if courses exist)
        if course_count > 0:
            avg = sum(courses.values()) / course_count
            if avg > best_avg:
                best_avg = avg
                best_avg_student = name

    if most_courses_student and max_courses >= 0:
        print(f"most courses completed {max_courses} {most_courses_student}")

    if best_avg_student and best_avg >= 0:
        print(f"best average grade {best_avg:.1f} {best_avg_student}")


if __name__ == "__main__":
    students = {}

    # --- Test 1: Adding students and printing initial state ---
    print("--- Test 1: Adding students & initial print ---")
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    print("-" * 30)

    # --- Test 2: Adding completed courses (Peter) ---
    print("--- Test 2: Adding courses (Peter) ---")
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")
    print("-" * 30)

    # --- Test 3: Repeating courses (Peter) ---
    print("--- Test 3: Repeating courses (Peter) ---")
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # Ignored (grade 0)
    add_course(students, "Peter", ("Data Structures and Algorithms", 0)) 
    # Ignored (grade 2 is lower than existing 3)
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")
    print("-" * 30)
    
    # Test case for grade improvement:
    print("--- Test 3b: Grade Improvement ---")
    add_course(students, "Peter", ("Advanced Course in Programming", 4)) # Improves grade from 2 to 4
    print_student(students, "Peter")
    print("-" * 30)

    # --- Test 4: Summary of database ---
    print("--- Test 4: Database Summary ---")
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1)) # Peter: 3 courses, avg 1.0
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4)) # Eliza: 2 courses, avg 4.5
    summary(students)


"""
# A square of letters
""" 

# The program asks for the number of layers and generates the concentric letter square pattern.

# 1. Read the number of layers (N) from the input.
# The standard 'input' function will display the prompt "Layers: " and wait for input.
layers_input = input("Layers: ")
N = int(layers_input)

# N is the number of layers (e.g., 3 for letters C, B, A)
# The side length of the square is 2*N - 1
S = 2 * N - 1
# The maximum index (row/col) is S - 1
M_idx = S - 1
# The index of the outermost letter (e.g., 'C' for N=3 is index 2)
Max_L = N - 1

# Iterate through rows (r) from 0 to S-1
for r in range(S):
    row_output = ""
    
    # Iterate through columns (c) from 0 to S-1
    for c in range(S):
        
        # Calculate the minimum distance D(r, c) to any edge of the square.
        # D(r, c) = min(dist_to_top, dist_to_bottom, dist_to_left, dist_to_right)
        dist_to_edge = min(r, M_idx - r, c, M_idx - c)
        
        # The letter index L (0=A, 1=B, 2=C, ...) is determined by:
        # L = Max_L - dist_to_edge
        # This maps the outermost ring (dist_to_edge=0) to the largest letter (Max_L), 
        # and the center (dist_to_edge=Max_L) to the 'A' letter (L=0).
        L = Max_L - dist_to_edge
        
        # Convert the index L to the corresponding character (e.g., 0 + ord('A') -> 'A')
        char = chr(ord('A') + L)
        row_output += char
        
    # Print the completed row
    print(row_output)