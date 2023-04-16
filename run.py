import os
import time


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
    print("A 3x3 board is printed and is marked 1-9.")
    print_board()
    print("\nWin: If 3 spots are filled in a row, column or diagonally.\n")
    print("Tie: The board is filled and 'X' or 'O' are not in a row.\n")
    print("Are you ready to play?\n")

    yes_no = input("Enter 'Y' for Yes - Enter 'N' for No: ")
    if yes_no == "y":
        print("\n\nThe game will start in 3 seconds.")
        time.sleep(3)
        os.system('clear')
        print_board()
    elif yes_no == "n":
        os.system('clear')
        print("\n\nPlease read the rules again.\n\n")
        print("They will appear in 3 seconds.")
        time.sleep(3)
        intro()
    else:
        os.system('clear')
        print(f"\n\nYou entered: '{yes_no}', Please enter 'y' or 'n'.\n")
        print("")
        intro()


# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
check_if_game_going = True
Winner = None

player_one = 0
player_two = 0


def print_board():
    """
    Displays the board for the game.
    """
    print("\nTic-Tac-Toe - 2 Player Edition\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")


intro()


def play_game():
    """
    Controls the game.
    While the game is running it places the 'X' or 'O'.
    Makes sure the game is running.
    Switches between 'X' and 'O'.
    Print who won or if the game is a draw.
    """

    global winner
    global check_if_game_going
    global current_player
    global player_one
    global player_two

    while check_if_game_going:
        handle_turn(current_player)

        check_is_gameover()

        flip_turns()

    if winner == "X":
        player_one += 1
        print("\nX won.")
    elif winner == "O":
        player_two += 1
        print("\nO won.")
    elif winner is None:
        print("Game is a draw.")


def handle_turn(player):
    """
    Allows the user to input a number from 1-9.
    Makes sure the number is between 1-9.
    Does not allow the user to input data into an already filled spot.
    """

    print(f"\n{player}'s turn.")
    position = input("\nChoose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("You entered incorrectly, Choose from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("\nSpot is already filled, please choose an empty spot.\n")

    board[position] = player
    os.system('clear')
    print_board()


def check_is_gameover():
    """
    Check carried out to see if the game is over.
    """
    check_for_win()
    check_for_tie()


def check_for_win():
    """
    Checks for a winner by checking rows, columns and diagonals.
    """

    global winner

    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None


def check_rows():
    """
    Check to see is there 3 matches in a row.
    """
    global check_if_game_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        check_if_game_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_columns():
    """
    Check to see is there 3 matches in a column.
    """
    global check_if_game_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        check_if_game_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


def check_diagonals():
    """
    Check to see is there 3 matches diagonally.
    """
    global check_if_game_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2:
        check_if_game_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]


def check_for_tie():
    """
    Checks to see if the game is a tie.
    """
    global check_if_game_going
    if "-" not in board:
        check_if_game_going = False


def flip_turns():
    """
    Switches the users turn.
    """
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

# Reset game.
# Option to play again.
# Option to reset leaderboard.
# Got help from the below link
# https://stackoverflow.com/questions/20667726/restart-a-tictactoe-game-after-a-win


while True:
    play_game()

    print(f"\nPlayer X's score: {player_one}")
    print(f"\nPlayer O's score: {player_two}")

    y_n = input("\nPlay again?\n Enter 'y' for Yes - Enter 'n' for No: ")
    if y_n == "y":
        print("")
    elif y_n == "n":
        print("We hope you enjoyed!")
        break
    else:
        break
    # Global variables for restarting the game
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    check_if_game_going = True
    winner = None
    current_player = "X"

    y_n = input("\nReset score?\n Enter 'y' for Yes - Enter 'n' for No: ")
    if y_n == "y":
        # resets score
        player_one = 0
        player_two = 0
        os.system('clear')
        print("Score reset.")
        print_board()
    elif y_n == "n":
        os.system('clear')
        print("Score not reset.")
        print_board()
