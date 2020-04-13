
class TicTacToeBoard:
    def __init__(self):
        self.state = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9
        ]

    def print_board(self):
        print(self.state[0], self.state[1], self.state[2], sep=" | ")
        print("---------")
        print(self.state[3], self.state[4], self.state[5], sep=" | ")
        print("---------")
        print(self.state[6], self.state[7], self.state[8], sep=" | ")

    def update_board(self, location, token):
        if self.valid_move(location):
            self.state[location - 1] = token
            return True
        else:
            return False

    def valid_move(self, location):
        return isinstance(self.state[location - 1], int)

    def check_board_filled(self):
        for location in self.state:
            if location is isinstance(location, int):
                return False
        return True

    def check_win(self):
        if self.check_rows():
            return True
        if self.check_columns():
            return True
        if self.check_diagonals():
            return True

        return False

    def __check_rows(self):
        return (self.state[0] == self.state[1] == self.state[2]) or \
               (self.state[3] == self.state[4] == self.state[5]) or \
               (self.state[6] == self.state[7] == self.state[8])

    def __check_columns(self):
        return (self.state[0] == self.state[3] == self.state[6]) or \
               (self.state[1] == self.state[4] == self.state[7]) or \
               (self.state[2] == self.state[5] == self.state[8])

    def __check_diagonals(self):
        return (self.state[0] == self.state[4] == self.state[8]) or (self.state[2] == self.state[4] == self.state[6])

