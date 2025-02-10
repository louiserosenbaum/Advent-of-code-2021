#Part 1
'''
with open('./day4input.txt') as f:
    data = f.read().strip().split("\n\n")  # Split into drawn numbers and boards

# Extract the drawn numbers
drawn_numbers = list(map(int, data[0].split(",")))  # Convert to list of integers

# Process the boards
boards = []
for board in data[1:]:  # Process each board
    newboard = [[int(num) for num in row.split()] for row in board.strip().split("\n")]
    boards.append(newboard)

# Create a helper function to check if a board has won
def check_winner(board, marked):
    """Checks if a board has a complete row or column marked."""
    for row in marked:
        if all(row):  # If all values in a row are True, it's a win
            return True
    for col in zip(*marked):  # Transpose the board to check columns
        if all(col):
            return True
    return False

# Initialize markers for all boards (same shape as board, filled with False)
marked_boards = [[[False] * 5 for _ in range(5)] for _ in boards]

# Play the game: Mark numbers and check for a winner
for number in drawn_numbers:
    for board_idx, board in enumerate(boards):
        # Mark the number on the board
        for r in range(5):
            for c in range(5):
                if board[r][c] == number:
                    marked_boards[board_idx][r][c] = True

        # Check if the board has won
        if check_winner(board, marked_boards[board_idx]):
            # Calculate the score
            unmarked_sum = sum(
                board[r][c] for r in range(5) for c in range(5) if not marked_boards[board_idx][r][c]
            )
            final_score = unmarked_sum * number
            print(f"Winning Board:\n{board}")
            print(f"Final Score: {final_score}")
            exit()  # Stop after finding the first winner
'''

#Part 2
with open('./day4input.txt') as f:
    data = f.read().strip().split("\n\n")  # Split into drawn numbers and boards

# Extract the drawn numbers
drawn_numbers = list(map(int, data[0].split(",")))  # Convert to list of integers

# Process the boards
boards = []
for board in data[1:]:  # Process each board
    newboard = [[int(num) for num in row.split()] for row in board.strip().split("\n")]
    boards.append(newboard)

# Create a helper function to check if a board has won
def check_winner(marked):
    """Checks if a board has a complete row or column marked."""
    for row in marked:
        if all(row):  # If all values in a row are True, it's a win
            return True
    for col in zip(*marked):  # Transpose the board to check columns
        if all(col):
            return True
    return False

# Initialize markers for all boards (same shape as board, filled with False)
marked_boards = [[[False] * 5 for _ in range(5)] for _ in boards]

# Track which boards have won
winning_boards = set()  # Store indices of winning boards
last_winning_idx = None  # Store the last board to win
last_winning_number = None  # Store the number that caused the last board to win

# Play the game: Mark numbers and track last winner
for number in drawn_numbers:
    for board_idx, board in enumerate(boards):
        if board_idx in winning_boards:  # Skip already winning boards
            continue

        # Mark the number on the board
        for r in range(5):
            for c in range(5):
                if board[r][c] == number:
                    marked_boards[board_idx][r][c] = True

        # Check if the board has won
        if check_winner(marked_boards[board_idx]):
            winning_boards.add(board_idx)  # Mark board as won
            last_winning_idx = board_idx  # Store the last winning board index
            last_winning_number = number  # Store the last drawn number

    # Stop when all boards have won
    if len(winning_boards) == len(boards):
        break  # Exit loop when the last board wins

# Calculate the final score for the last winning board
if last_winning_idx is not None:
    last_board = boards[last_winning_idx]  # Retrieve the actual last board
    last_marked = marked_boards[last_winning_idx]  # Retrieve its marking status

    unmarked_sum = sum(
        last_board[r][c]
        for r in range(5)
        for c in range(5)
        if not last_marked[r][c]
    )
    final_score = unmarked_sum * last_winning_number

    print(f"Last Winning Board:\n{last_board}")
    print(f"Final Score: {final_score}")