"""
# https://programming-25.mooc.fi/part-5/1-more-lists
""" 

"""
# The longest string
""" 

def longest(strings: list) -> str:

    # Check if the list is empty. While the problem assumes a single longest string,
    # handling an empty list is good practice (returning None or raising an error).
    if not strings:
        return None 

    # Initialize the longest string found so far with the first string in the list.
    longest_string = strings[0]
    
    # Iterate through the rest of the strings in the list.
    # We can start from the second element (index 1) or iterate through all elements.
    for current_string in strings[1:]:
        
        # Compare the length of the current string with the length of the longest 
        # string found so far.
        if len(current_string) > len(longest_string):
            
            # If the current string is longer, update the longest_string variable.
            longest_string = current_string
            
    # Return the string that has the maximum length after checking all elements.
    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

    # Another example
    strings_2 = ["short", "medium", "longer string", "S"]
    print(longest(strings_2))

"""
# Number of matching elements
""" 
    
def count_matching_elements(my_matrix: list, element: int) -> int:
    """
    Counts how many elements within a two-dimensional array (matrix) 
    match a given integer value.

    Args:
        my_matrix: A list of lists representing the matrix of integers.
        element: The integer value to search for and count.

    Returns:
        The total count of matching elements.
    """
    
    count = 0  # Initialize the counter for matching elements.
    
    # Outer loop: Iterate through each row (inner list) in the matrix.
    for row in my_matrix:
        
        # Inner loop: Iterate through each individual number within the current row.
        for number in row:
            
            # Check if the current number matches the target element.
            if number == element:
                count += 1  # If it matches, increment the counter.
                
    return count

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    
    # Example 1: Count how many '1's are in the matrix.
    print(count_matching_elements(m, 1))
    
    # Example 2: Count how many '0's are in the matrix.
    print(count_matching_elements(m, 0))
    
    # Example 3: Count how many '5's (should be 0).
    m2 = [[5, 5], [5, 5], [1, 2]]
    print(count_matching_elements(m2, 5))


"""
# Go
""" 
def who_won(game_board: list) -> int:
    """
    Determines the winner of a simplified game of Go by comparing the number 
    of pieces each player has on the board.

    0: empty square, 1: player 1 piece, 2: player 2 piece

    Args:
        game_board: A list of lists representing the board state.

    Returns:
        1 if Player 1 won, 2 if Player 2 won, or 0 for a tie.
    """
    
    player1_count = 0
    player2_count = 0
    
    # Iterate through each row of the game board
    for row in game_board:
        # Iterate through each piece in the current row
        for piece in row:
            if piece == 1:
                player1_count += 1
            elif piece == 2:
                player2_count += 1
            # We ignore piece == 0 (empty square)
                
    # Compare the counts to determine the winner
    if player1_count > player2_count:
        return 1  # Player 1 wins
    elif player2_count > player1_count:
        return 2  # Player 2 wins
    else:
        return 0  # It's a tie (draw)

if __name__ == "__main__":
    # Player 1 (1s): 4 | Player 2 (2s): 3 -> Player 1 wins (1)
    game_1 = [[1, 2, 1], 
              [0, 2, 1], 
              [1, 2, 0]]
    print(f"Game 1 result: {who_won(game_1)}") 
    
    # Player 1 (1s): 2 | Player 2 (2s): 2 -> Tie (0)
    game_2 = [[2, 2], 
              [1, 1]]
    print(f"Game 2 result: {who_won(game_2)}")
    
    # Player 1 (1s): 0 | Player 2 (2s): 5 -> Player 2 wins (2)
    game_3 = [[0, 2, 2], 
              [0, 2, 2], 
              [0, 0, 0]]
    print(f"Game 3 result: {who_won(game_3)}")



"""
# Sudoku: check row
""" 

def row_correct(sudoku: list, row_no: int) -> bool:
    """
    Checks if a specified row in a Sudoku grid is valid. A row is valid if 
    it contains each of the numbers 1 to 9 at most once (ignoring 0s).

    Args:
        sudoku: A 2D list representing the Sudoku grid.
        row_no: The index of the row to check (0-indexed).

    Returns:
        True if the row is correct, False otherwise.
    """
    
    # 1. Get the specific row
    row = sudoku[row_no]
    
    # 2. Filter out all the zeros (empty squares)
    # We only want to check the filled numbers (1-9) for duplicates.
    filled_numbers = [number for number in row if number != 0]
    
    # 3. Check for duplicates using a set
    # A set only stores unique elements. If the list of filled numbers 
    # is the same length as the set created from it, there are no duplicates.
    
    unique_numbers = set(filled_numbers)
    
    if len(filled_numbers) == len(unique_numbers):
        return True
    else:
        return False

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],  # Row 0: Filled numbers are [9, 8, 3]. All unique. -> True
        [2, 0, 0, 2, 5, 0, 7, 0, 0],  # Row 1: Filled numbers are [2, 2, 5, 7]. '2' is duplicated. -> False
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(f"Row 0 correct: {row_correct(sudoku, 0)}")
    print(f"Row 1 correct: {row_correct(sudoku, 1)}")
    print(f"Row 3 correct: {row_correct(sudoku, 3)}") # [2, 9, 4] -> True


"""
# Sudoku: check column
""" 
def column_correct(sudoku: list, column_no: int) -> bool:
    """
    Checks if a specified column in a Sudoku grid is valid. A column is valid if 
    it contains each of the numbers 1 to 9 at most once (ignoring 0s).

    Args:
        sudoku: A 2D list representing the Sudoku grid.
        column_no: The index of the column to check (0-indexed).

    Returns:
        True if the column is correct, False otherwise.
    """
    
    # 1. Extract the specific column
    column = []
    
    # Iterate through each row and pick the element at the specified column_no
    for row in sudoku:
        column.append(row[column_no])
        
    # 2. Filter out all the zeros (empty squares)
    # We only want to check the filled numbers (1-9) for duplicates.
    filled_numbers = [number for number in column if number != 0]
    
    # 3. Check for duplicates using a set
    # If the list of filled numbers is the same length as the set created 
    # from it, there are no duplicates, and the column is correct.
    
    unique_numbers = set(filled_numbers)
    
    # The column is correct if the count of filled numbers equals the count of unique filled numbers
    if len(filled_numbers) == len(unique_numbers):
        return True
    else:
        return False

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    # Column 0: [9, 2, 0, 2, 0, 7, 0, 0, 3]. '2' is duplicated. -> False
    print(f"Column 0 correct: {column_correct(sudoku, 0)}") 
    
    # Column 1: [0, 0, 2, 9, 0, 0, 0, 0, 0]. Filled numbers [2, 9]. All unique. -> True
    print(f"Column 1 correct: {column_correct(sudoku, 1)}") 
    
    # Column 4: [8, 5, 0, 0, 3, 6, 0, 0, 0]. Filled numbers [8, 5, 3, 6]. All unique. -> True
    print(f"Column 4 correct: {column_correct(sudoku, 4)}")


"""
# Sudoku: check block
""" 
def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    """
    Checks if the 3x3 block starting at the specified (row_no, column_no) 
    is valid. A block is valid if it contains each of the numbers 1 to 9 
    at most once (ignoring 0s).

    Args:
        sudoku: A 2D list representing the Sudoku grid.
        row_no: The starting row index of the 3x3 block (0-indexed).
        column_no: The starting column index of the 3x3 block (0-indexed).

    Returns:
        True if the block is correct, False otherwise.
    """
    
    block_numbers = []
    
    # Iterate through the 3 rows that form the block
    for r in range(row_no, row_no + 3):
        # Iterate through the 3 columns that form the block
        for c in range(column_no, column_no + 3):
            # Append the number to our list
            block_numbers.append(sudoku[r][c])
            
    # 1. Filter out all the zeros (empty squares)
    filled_numbers = [number for number in block_numbers if number != 0]
    
    # 2. Check for duplicates using a set
    # If the number of filled elements equals the number of unique filled elements, 
    # there are no duplicates, and the block is correct.
    unique_numbers = set(filled_numbers)
    
    if len(filled_numbers) == len(unique_numbers):
        return True
    else:
        return False

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    # Block 1 (0, 0): [9, 0, 0, 2, 0, 0, 0, 2, 0]. Contains duplicate '2'. -> False
    print(f"Block at (0, 0) correct: {block_correct(sudoku, 0, 0)}")
    
    # Block 2 (1, 2): [0, 2, 5, 0, 3, 0, 4, 0, 0]. Filled numbers: [2, 5, 3, 4]. All unique. -> True
    print(f"Block at (1, 2) correct: {block_correct(sudoku, 1, 2)}")

    # Block 3 (6, 6) - bottom right standard block. Filled numbers: [9, 0, 0, 0, 0, 3, 0, 0, 2]. -> True
    print(f"Block at (6, 6) correct: {block_correct(sudoku, 6, 6)}")


"""
# Sudoku: check grid
""" 
def row_correct(sudoku: list, row_no: int) -> bool:
    """Checks if a specified row is valid (no duplicates among 1-9, ignoring 0)."""
    row = sudoku[row_no]
    filled_numbers = [number for number in row if number != 0]
    # A row is correct if the count of filled numbers equals the count of unique filled numbers
    return len(filled_numbers) == len(set(filled_numbers))

def column_correct(sudoku: list, column_no: int) -> bool:
    """Checks if a specified column is valid (no duplicates among 1-9, ignoring 0)."""
    # Extract the column
    column = [row[column_no] for row in sudoku]
    filled_numbers = [number for number in column if number != 0]
    # A column is correct if the count of filled numbers equals the count of unique filled numbers
    return len(filled_numbers) == len(set(filled_numbers))

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    """Checks if the 3x3 block starting at (row_no, column_no) is valid (no duplicates)."""
    
    block_numbers = []
    
    # Iterate through the 3 rows and 3 columns that form the block
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            block_numbers.append(sudoku[r][c])
            
    # Filter out empty squares (0s)
    filled_numbers = [number for number in block_numbers if number != 0]
    
    # A block is correct if the count of filled numbers equals the count of unique filled numbers
    return len(filled_numbers) == len(set(filled_numbers))

def sudoku_grid_correct(sudoku: list) -> bool:
    """
    Determines whether the 9x9 Sudoku grid is filled in correctly 
    by checking all 9 rows, 9 columns, and 9 standard 3x3 blocks.
    
    Returns True if all are correct, False if any single one fails.
    """
    
    # 1. Check all 9 Rows and all 9 Columns
    for i in range(9):
        # Check Row i
        if not row_correct(sudoku, i):
            return False
        # Check Column i
        if not column_correct(sudoku, i):
            return False
            
    # 2. Check all 9 Standard 3x3 Blocks
    # Iterate through the starting indices of the nine blocks: (0, 0), (0, 3), (0, 6), etc.
    for r_start in range(0, 9, 3):
        for c_start in range(0, 9, 3):
            if not block_correct(sudoku, r_start, c_start):
                return False
            
    # If all 27 checks pass (9 rows + 9 columns + 9 blocks)
    return True

if __name__ == "__main__":
    sudoku1 = [
      [9, 0, 0, 0, 8, 0, 3, 0, 0],
      [2, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [2, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]]
      
    sudoku2 = [
      [2, 6, 7, 8, 3, 9, 5, 0, 4],
      [9, 0, 3, 5, 1, 0, 6, 0, 0],
      [0, 5, 1, 6, 0, 0, 8, 3, 9],
      [5, 1, 9, 0, 4, 6, 3, 2, 8],
      [8, 0, 2, 1, 0, 5, 7, 0, 6],
      [6, 7, 4, 3, 2, 0, 0, 0, 5],
      [0, 0, 0, 4, 5, 7, 2, 6, 3],
      [3, 2, 0, 0, 8, 0, 0, 5, 7],
      [7, 4, 5, 0, 0, 3, 9, 0, 1]]
      
    print(sudoku_grid_correct(sudoku1)) 
    print(sudoku_grid_correct(sudoku2))