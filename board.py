
class TicTacToeBoard:
    def __init__(self):
        self.state = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9
        ]
        self.turn = 0
        self.p1 = 'x'
        self.p2 = 'o'

    def update_board(self, space):
        if self.turn == 0:
            self.state[space - 1] = self.p1
            self.turn = 1
        else:
            self.state[space - 1] = self.p2
            self.turn = 0

    def check_game_end(self):
        # check if last move won game

        # check if game spots are filled
        for space in self.state:
            if space is None:
                return False

x = TicTacToeBoard()

print(x.state)

