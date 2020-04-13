from board import Board
from player import Player
import pdb

class TicTacToe:
    status = "initiated"
    players = []
    board = None
    current_player_index = 0


    def __init__(self):
        self.board = Board()

    def add_player(self, player):
        self.players += [player]

    def execute_turn(self):
        location = self.__prompt_move()
        token = self.__get_current_token()
        if self.board.valid_move(location, token):
            self.board.update_board(location, token)
            self.__update_game_state()
        else:
            raise Exception("Invalid move")

    def start(self):
        print("This game requires 2 players.")
        self.add_player(self.__prompt_add_player('player1', 'X'))
        self.add_player(self.__prompt_add_player('player2', 'O'))
        self.execute_turn()

    def __get_current_token(self):
        current_player = self.__get_current_player()
        return current_player.token

    def __get_current_player(self):
        return self.players[self.current_player_index]

    def __prompt_add_player(self, title, default_token):
        name = input(f"Enter name for {title}: ")
        should_create_token = input(f"Use custom token for {name}?(y/n) ")
        if should_create_token == 'y':
            token = list(input("Enter single character for token: "))[0]
        else:
            token = default_token
        return Player(name, token)

    def __prompt_move(self):
        return input("Where do you want to place your token?")

    def __switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def __update_game_state(self):
        if self.board.has_3_in_a_row(self.__get_current_token()):
            self.status = "ended"
        else:
            self.__switch_player()

# starter code
game = TicTacToe()
game.start()
print(game.players[0].name, game.players[0].token)
print(game.players[1].name, game.players[1].token)
print(game.current_player_index)