"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/22/2020
Homework : Final Term Project
Description: A console based Tic Tac Toe game

"""

import GameController


class GameBoard:
    """
    A class that is for creating a tic tac toe game board
    This class holds properties and methods that are relative to itself and
    its responsibilities.
    """

    # Game mode should be only 2 values: PvP or PvC
    board_game_mode = None

    # Players value should be either X or O, one or the other combined between
    # the two properties
    player_one_char = None
    player_two_char = None

    current_payer_turn = None
    player_winner = None

    # A dictionary for mapping the values for the game board in text, making
    # programmatic setter/getter access easy and fast
    __data_board = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
    }

    def get_str_board(self):
        """
        Custom Game board made of text with ASCII art pattern.
        This string is hooked with with the `data_board` values via `format`.
        method, accessible public method

        :return: String text
        """
        return """
        *************************
        *       *       *       *
        *  {}   *  {}   *  {}   *
        *       *       *       *
        *************************
        *       *       *       *
        *  {}   *  {}   *  {}   *
        *       *       *       *
        *************************
        *       *       *       *
        *  {}   *  {}   *  {}   *
        *       *       *       *
        *************************
        """.format(
                f" {self.__data_board[1]}"
                if self.__data_board[1] is not "" else " 1",

                f" {self.__data_board[2]}"
                if self.__data_board[2] is not "" else " 2",

                f" {self.__data_board[3]}"
                if self.__data_board[3] is not "" else " 3",

                f" {self.__data_board[4]}"
                if self.__data_board[4] is not "" else " 4",

                f" {self.__data_board[5]}"
                if self.__data_board[5] is not "" else " 5",

                f" {self.__data_board[6]}"
                if self.__data_board[6] is not "" else " 6",

                f" {self.__data_board[7]}"
                if self.__data_board[7] is not "" else " 7",

                f" {self.__data_board[8]}"
                if self.__data_board[8] is not "" else " 8",

                f" {self.__data_board[9]}"
                if self.__data_board[9] is not "" else " 9"
        )

    def set_input_to_board(self, move):
        """
        A method for setting values to board
        :param move: Tuple
        :return: Boolean
        """
        if not self.__validate_move_taken(move):
            return False

        i, v = move
        self.__data_board[i] = v
        return True

    def __validate_move_taken(self, move):
        """
        A method for validating the value before inserting it
        :param move: Tuple
        :return: Boolean
        """

        if type(move) is not tuple:
            return False

        i, v = move

        if self.__data_board[i] == str(""):
            return True

        return False

    def data_pass_delegate(self, eval_caller):
        """
        A method binder to pass data
        :param eval_caller: function caller
        :return: the data board
        """
        if eval_caller.__name__ == GameController.validate_winner.__name__:
            return self.__data_board
        else:
            return None

    def reset_game_board(self):
        """
        A method to reset the board values
        """
        self.board_game_mode = None
        self.player_one_char = None
        self.player_two_char = None
        self.current_payer_turn = None
        self.player_winner = None

        self.__data_board = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: "",
        }

    def __init__(self, mode, p1):
        """
        The init method of the class
        :param mode: the mode for the game
        :param p1: The player 1 character
        """
        self.board_game_mode = mode
        self.player_one_char = p1

        if p1 is "X":
            self.player_two_char = "O"

        if p1 is "O":
            self.player_two_char = "X"

