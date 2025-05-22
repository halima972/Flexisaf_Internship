# creating an empty 3x3 matrix to define the game board
def main_game_loop():
    game_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
# Keep track of whose turn it is
    current_player = 'X' 
    game_over = False

    # The game continues as long as it's not over
    while not game_over:
        # Display the board at the start of each turn
        display_board(game_board)
        # Allow the current player to make a move
        print(f"\nIt's Player {current_player}'s turn.")
        make_move(game_board, current_player)

        # Check if the current player has won
        if check_win(game_board, current_player):
            display_board(game_board) 
            print(f"\n🎉 Congratulations! Player {current_player} wins! 🎉")
            game_over = True 
        # If not a win, check if the game is a tie
        elif check_tie(game_board): 
            display_board(game_board) # Show the final tied board
            print("\nIt's a Tie! The board is full and no one won.")
            game_over = True 
        else:
            # If neither a win nor a tie, switch to the other player's turn
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

# displaying the board to look user-friendly
def display_board(game_board):
    print("-------------") # for the top boarder
    for i in range(3):
        print(f"| {game_board[i][0]} | {game_board[i][1]} | {game_board[i][2]} |")
        if i<2:
            print("-------------")
    print("-------------") # for the bottom boarder

# variable for the player
player = print(input("X or O:"))  

# craeting a function for making a move in the game
def make_move(game_board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            # Check if row and column are within bounds (0 to 2)
            if 0 <= row <= 2 and 0 <= col <= 2:
                # Check if the chosen cell is empty
                if game_board[row][col] == ' ':
                    game_board[row][col] = player  # Update the board with the player's move
                    break  
                else:
                    print("That spot is already taken! Please choose an empty spot.")
            else:
                print("Row and column must be between 0 and 2. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.") 
    
# to for Wins or lose
def check_win(game_board, player):
    # Check rows
    for row in range(3):
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            return True

    # Check columns
    for col in range(3):
        if game_board[0][col] == player and game_board[1][col] == player and game_board[2][col] == player:
            return True

    # Check main diagonal (top-left to bottom-right)
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        return True

    # Check anti-diagonal (top-right to bottom-left)
    if game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        return True

    # If no win condition is met
    return False

#Checking for tie
def check_tie(game_board):
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == ' ':
                return False  # Found an empty spot, so not a tie
    return True

def ai_move(game_board, ai_player, human_player):
    # Rule 1: Check if AI can win in the next move
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == ' ': # If the spot is empty
                game_board[row][col] = ai_player # Simulate AI's move
                if check_win(game_board, ai_player):
                    return # AI wins, move is made permanently
                else:
                    game_board[row][col] = ' ' # Undo the simulated move

    # Rule 2: Check if human can win in their next move (and block it)
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == ' ': # If the spot is empty
                game_board[row][col] = human_player # Simulate human's move
                if check_win(game_board, human_player):
                    game_board[row][col] = ai_player 
                    return 
                else:
                    game_board[row][col] = ' ' # Undo the simulated human move

    for row in range(3):
        for col in range(3):
            if game_board[row][col] == ' ':
                game_board[row][col] = ai_player
                return # Move made, exit function

print("Welcome to Tic-Tac-Toe!")
main_game_loop()