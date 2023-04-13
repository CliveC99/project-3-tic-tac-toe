
def intro():
    """
    Gives the user information and rules about the games.
    Allows the user to start the game by entering 'y'.
    Catches error for data input incorrectly.
    """
    print("Welcome to Tic-Tac-Toe, 2 player edition!")
    print("\nRules:\n")
    print("Player 1 is given 'X'")
    print("Player 2 is given 'O'\n")
    print("A 3x3 board is printed and is marked 1-9\n")
    print("Win: If 3 spots are filled in a row, column or diagonally.\n")
    print("Tie: The board is filled and 'X' or 'O' are not in a row.\n")
    print("Are you ready to play?\n")
intro()   


# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]



def print_board():
    """
    Displays the board for the game.
    """
    print(board[0] + " | " + board[1] + " | " + board[2] + "")
    print(board[3] + " | " + board[4] + " | " + board[5] + "")
    print(board[6] + " | " + board[7] + " | " + board[8] + "")

print_board()
