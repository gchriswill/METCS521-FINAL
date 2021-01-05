"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/22/2020
Homework : Final Term Project
Description: A console based Tic Tac Toe game

"""

from GameBoard import GameBoard
import GameController


def run_game_program(game_board_param: GameBoard):
    """
    The main function in which the game runs
    :param game_board_param: GameBoard
    """

    while True:

        player_turn = GameController.player_next_turn(game_board_param)

        if player_turn:
            player_win = game_board_param.current_payer_turn
            print(f"Congratulations, Player {player_win} have won!")
            GameController.end_game(game_board_param)
            break


if __name__ == "__main__":
    print("Welcome to our Tic Tac Toe game!")
    game_board = GameController.start_game()
    run_game_program(game_board)
    exit("The game has ended...")