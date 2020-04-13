class Player:
    def __init__(self, name, token=None):
        self.name = name
        self.token = token

    def change_token(self, token):
        self.token = token
