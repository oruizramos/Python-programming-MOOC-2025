"""
# https://programming-25.mooc.fi/part-5/2-references
""" 

"""
# Items multiplied by two
""" 

def double_items(numbers: list) -> list:
    """
    Takes a list of integers and returns a new list where all values are doubled.
    
    The original list remains unchanged.

    Args:
        numbers: The list of integers to be doubled.

    Returns:
        A new list containing the doubled values.
    """
    # Use a list comprehension to iterate through the original list and multiply each item by 2.
    # This automatically creates and returns a brand new list.
    return [item * 2 for item in numbers]

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    
    # Print both lists to verify the original was not changed
    print("original:", numbers)
    print("doubled:", numbers_doubled)



"""
# Remove the smallest
""" 

def remove_smallest(numbers: list):
    """
    Finds and removes the smallest item from the given list of integers in place.
    
    This function modifies the original list and has no return value.
    Assumes there is a single smallest item.

    Args:
        numbers: The list of integers to modify.
    """
    if not numbers:
        # Handle the case of an empty list, though the problem description
        # implies the list will contain elements.
        return
        
    # 1. Find the smallest value in the list
    smallest_value = min(numbers)
    
    # 2. Remove the first occurrence of that smallest value from the list
    # The list.remove() method modifies the list in place, fulfilling the requirement.
    numbers.remove(smallest_value)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    print("List before modification:", numbers)
    
    # Call the function (note: it does not return anything)
    remove_smallest(numbers)
    
    # Print the list after modification
    print("List after modification:", numbers) 
    
    # Test with another case
    numbers_two = [10, 5, 20, 5, 30]
    print("\nSecond list before modification:", numbers_two)
    remove_smallest(numbers_two)
    print("Second list after removing one '5':", numbers_two)


"""
# Sudoku: print out the grid and add a number
""" 

def print_sudoku(sudoku: list):
    """
    Prints a 9x9 Sudoku grid.
    Zeros are displayed as underscores (_).
    Horizontal and vertical separators are added every 3 cells/rows.

    Args:
        sudoku: A 9x9 two-dimensional list of integers (0-9).
    """
    for r in range(9):
        # Iterate through columns
        for c in range(9):
            cell_value = sudoku[r][c]
            
            # Determine the character to print: the number or an underscore for 0
            char_to_print = str(cell_value) if cell_value != 0 else "_"
            
            # Print the character followed by a space
            print(char_to_print, end=" ")
            
            # Add an extra space every 3 columns (index 2 and 5) for the vertical grid lines
            if c == 2 or c == 5:
                print(" ", end="")
        
        # Print a newline at the end of the row
        print()
        
        # Add a blank line every 3 rows (index 2 and 5) for the horizontal grid lines
        # but avoid adding one after the very last row (r=8)
        if (r == 2 or r == 5) and r < 8:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    """
    Adds a digit to the specified location in the Sudoku grid.
    The function modifies the list in place (no return value).

    Args:
        sudoku: The 9x9 two-dimensional list representing the Sudoku grid.
        row_no: The zero-based row index (0-8).
        column_no: The zero-based column index (0-8).
        number: The digit to place in the cell (1-9).
    """
    # Directly assign the number to the specified location in the 2D list
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    # Initial empty 9x9 Sudoku grid
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print_sudoku(sudoku)
    
    # Add numbers to the grid
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    
    print()
    print("Three numbers added:")
    print()
    
    print_sudoku(sudoku)


"""
# Sudoku: add number to a copy of the grid
""" 

def print_sudoku(sudoku: list):
    """
    Prints a 9x9 Sudoku grid.
    Zeros are displayed as underscores (_).
    Horizontal and vertical separators are added every 3 cells/rows.

    Args:
        sudoku: A 9x9 two-dimensional list of integers (0-9).
    """
    for r in range(9):
        # Iterate through columns
        for c in range(9):
            cell_value = sudoku[r][c]
            
            # Determine the character to print: the number or an underscore for 0
            char_to_print = str(cell_value) if cell_value != 0 else "_"
            
            # Print the character followed by a space
            print(char_to_print, end=" ")
            
            # Add an extra space every 3 columns (index 2 and 5) for the vertical grid lines
            if c == 2 or c == 5:
                print(" ", end="")
        
        # Print a newline at the end of the row
        print()
        
        # Add a blank line every 3 rows (index 2 and 5) for the horizontal grid lines
        if (r == 2 or r == 5) and r < 8:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    """
    Returns a copy of the original Sudoku grid with the new digit added.
    The original grid is NOT modified.

    Args:
        sudoku: The 9x9 two-dimensional list representing the Sudoku grid.
        row_no: The zero-based row index (0-8).
        column_no: The zero-based column index (0-8).
        number: The digit to place in the cell (1-9).
        
    Returns:
        A new 9x9 Sudoku grid list with the added number.
    """
    # Create a deep copy of the 2D list. 
    # This list comprehension copies each inner list (row) independently,
    # ensuring the original 'sudoku' list is never changed.
    new_sudoku = [row[:] for row in sudoku]
    
    # Add the number to the copy
    new_sudoku[row_no][column_no] = number
    
    return new_sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Call the function and store the returned copy
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    
    print("Original:")
    print_sudoku(sudoku)
    
    print()
    
    print("Copy:")
    print_sudoku(grid_copy)


"""
# Tic-Tac-Toe
""" 

def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    """
    Attempts to place a symbol (piece) on the Tic-Tac-Toe game board 
    at the given column (x) and row (y) coordinates.

    Args:
        game_board: A 3x3 two-dimensional list of strings ("X", "O", or "").
        x: The column index (0, 1, or 2).
        y: The row index (0, 1, or 2).
        piece: The symbol to place ("X" or "O").

    Returns:
        True if the move was successful (square was empty and coordinates valid), 
        False otherwise.
    """
    
    # 1. Coordinate Validation: Check if x and y are within the valid 0-2 range
    if not (0 <= x <= 2 and 0 <= y <= 2):
        print(f"Error: Invalid coordinates ({x}, {y}). Coordinates must be between 0 and 2.")
        return False

    # 2. Occupancy Check: Check if the square is currently empty ("")
    # Note: game_board is accessed as [row][column] or [y][x]
    if game_board[y][x] == "":
        # Square is empty, so place the piece
        game_board[y][x] = piece
        return True
    else:
        # Square is already occupied
        print(f"Error: Square at ({x}, {y}) is already occupied by '{game_board[y][x]}'.")
        return False

# Example Execution:
game_board = [["", "", ""], ["", "", ""], ["", "", ""]]

print(play_turn(game_board, 2, 0, "X"))
print(game_board)

# Example of a failed move (occupied square)
print("\nAttempting to move to occupied square (2, 0):")
print(play_turn(game_board, 2, 0, "O"))
print(game_board)

# Example of a failed move (invalid coordinates)
print("\nAttempting to move to invalid coordinate (3, 1):")
print(play_turn(game_board, 3, 1, "O"))
print(game_board)


"""
# Transpose a matrix
""" 

def transpose(matrix: list):
    """
    Transposes a square matrix in-place by swapping elements across 
    its main diagonal. The function modifies the original matrix 
    passed as an argument and has no return value.

    Args:
        matrix: A square two-dimensional list of integers.
    """
    
    # Assuming the matrix is square, we get the size N (number of rows/columns)
    N = len(matrix)
    
    # Iterate through the rows (i)
    for i in range(N):
        # Iterate through the columns (j), starting from i + 1.
        # Starting from i + 1 ensures that:
        # 1. The elements on the main diagonal (where i == j) are skipped.
        # 2. Each pair (i, j) and (j, i) is swapped exactly once.
        for j in range(i + 1, N):
            
            # Perform the swap: matrix[i][j] <-> matrix[j][i]
            # This is a Pythonic way to swap two values efficiently.
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Helper function to print the matrix cleanly for demonstration
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Example execution:
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
print_matrix(matrix_a)
print("-" * 15)

transpose(matrix_a)

print("Transposed matrix:")
print_matrix(matrix_a)

print("\n--- Another example ---")
matrix_b = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
]

print("Original matrix B:")
print_matrix(matrix_b)
print("-" * 15)

transpose(matrix_b)

print("Transposed matrix B:")
print_matrix(matrix_b)

