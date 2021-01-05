
"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/22/2020
Homework : Final Term Project
Description: A console based Tic Tac Toe game

"""

import GameBoard
from random import randint
from string import digits


class GameInvalidInput(Exception):
    """
    A class for holding the input string errors
    """
    generic_input_error = "Invalid input received. Please try again..."
    empty_input_error = "Empty input received. Please try again..."
    more_input_error = "More input received than expected. Please try again..."

    invalid_move_input_error = "Invalid input received. Please enter 1 tru 9"
    invalid_char_input_error = "Invalid input received. Please enter X or O"
    invalid_mode_input_error = "Invalid input received. Please enter PvP or PvC"


class GameInvalidAction(Exception):
    """
    A class for holding the action errors
    """
    generic_action_error = "Invalid action received. Please try again..."


def start_game():
    """
    The main method to start the game
    :return: Game Board
    """
    print("Starting Tic Tac Toe Game")

    mode_user_input = collect_mode()
    char_user_input = collect_char()

    return GameBoard.GameBoard(mode_user_input, char_user_input)


def end_game(board: GameBoard):
    """
    The method to end the game
    :param board: GameBoard
    """
    print("Ending Tic Tac Toe Game")
    #
    # File generator
    # Logic took me some time and didn't had enough more to implement the file
    # input/output
    #
    board.reset_game_board()


def computer_move():
    # Logic took me some time and didn't had enough more to implement the file
    # Player VS Computer mechanics
    return randint(1, 9)


def player_move(game_board: GameBoard, move):
    """
    The method in which executes a player move
    :param game_board: GameBoard
    :param move: Move Tuple
    :return: Boolean
    """
    set_success = game_board.set_input_to_board(move)
    if not set_success:
        raise GameInvalidInput(GameInvalidInput.generic_input_error)
    if validate_winner(move, game_board):
        return True
    else:
        return False


def player_next_turn(game_board: GameBoard):
    """
    The method for ever player turn
    :param game_board: GameBoard
    :return: Boolean
    """

    print("Tic Tac Toe: Available locations")
    print(game_board.get_str_board())

    print("Tic Tac Toe: Player turns")
    if game_board.current_payer_turn is None:
        print("Player one always starts the first turn...")
        game_board.current_payer_turn = game_board.player_one_char
        tuple_move = collect_move(game_board), game_board.current_payer_turn
        return player_move(game_board, tuple_move)
    else:
        if game_board.current_payer_turn == "X":
            game_board.current_payer_turn = "0"
            tuple_move = collect_move(game_board), game_board.current_payer_turn
            return player_move(game_board, tuple_move)
        else:
            game_board.current_payer_turn = "X"
            tuple_move = collect_move(game_board), game_board.current_payer_turn
            return player_move(game_board, tuple_move)


# Game Controller collectors
def collect_mode():
    """
    Method for collecting the mode of the game
    :return: Mode input
    """
    while True:
        mode_user_input = input("Please enter the game mode: PvP or PvC")
        mode_validated = validate_mode_input(mode_user_input)

        try:
            if mode_validated is None:
                break
            else:
                if type(mode_validated) is GameInvalidInput:
                    raise mode_validated
        except GameInvalidInput as e:
            print(f"{e.__class__.__name__}: {str(e.args[0])}")

    return mode_user_input


def collect_char():
    """
    Method for collecting the character of the player
    :return: Char input
    """
    while True:
        char_user_input = input("Player 1: Choose your Char now: X or O")
        char_validated = validate_char_input(char_user_input)

        try:
            if char_validated is None:
                break
            else:
                if type(char_validated) is GameInvalidInput:
                    raise char_validated
        except GameInvalidInput as e:
            print(f"{e.__class__.__name__}: {str(e.args[0])}")

    return char_user_input


def collect_move(game_board: GameBoard):
    input_message = f"Player with `{game_board.current_payer_turn}`: " \
                    f"Play your move with an available number to place " \
                    f"your Char in the designated location from the board."
    while True:
        move_user_input = input(input_message)
        move_validated = validate_move_input(move_user_input)

        try:
            if move_validated is None:
                break
            else:
                if type(move_validated) is GameInvalidInput:
                    raise move_validated
        except GameInvalidInput as e:
            print(f"{e.__class__.__name__}: {str(e.args[0])}")

    return int(move_user_input)


# Game Controller validators
def validate_mode_input(input_param):
    str_input = str(input_param).strip()
    validated = validate_input_preconditions(input_param)

    if validated is not None:
        return validated

    if str_input == str("PvP"):
        # or str_input == str("PvC"):
        return None

    return GameInvalidInput(GameInvalidInput.invalid_mode_input_error)


def validate_char_input(input_param):
    str_input = str(input_param).strip().upper()
    validated = validate_input_preconditions(input_param)

    if validated is not None:
        return validated

    if str_input == str("X") or str_input == str("O"):
        return None

    return GameInvalidInput(GameInvalidInput.invalid_char_input_error)


def validate_move_input(input_param):
    int_input = input_param
    validated = validate_input_preconditions(int_input)

    if validated is not None:
        return validated

    if int_input in digits.replace("0", ""):
        return None

    return GameInvalidInput(GameInvalidInput.invalid_move_input_error)


def validate_input_preconditions(input_param):

    if len(input_param) == 0:
        return GameInvalidInput(GameInvalidInput.empty_input_error)

    if input_param == "":
        return GameInvalidInput(GameInvalidInput.empty_input_error)

    return None


def validate_winner(move, game_board: GameBoard):
    """
    Method for validating who wins
    :param move: Move Tuple
    :param game_board: GameBoard
    :return: Boolean
    """
    _, char = move
    data_board = game_board.data_pass_delegate(validate_winner)

    if data_board is None:
        raise GameInvalidAction(GameInvalidAction.generic_action_error)

    if data_board[1] == data_board[2] == data_board[3] == char:
        return True

    if data_board[4] == data_board[5] == data_board[6] == char:
        return True

    if data_board[7] == data_board[8] == data_board[9] == char:
        return True

    if data_board[1] == data_board[4] == data_board[7] == char:
        return True

    if data_board[2] == data_board[5] == data_board[8] == char:
        return True

    if data_board[3] == data_board[6] == data_board[9] == char:
        return True

    if data_board[1] == data_board[5] == data_board[9] == char:
        return True

    if data_board[3] == data_board[5] == data_board[7] == char:
        return True

    return False

