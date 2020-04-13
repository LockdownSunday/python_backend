#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Runner:
    game = None

    def __init__(self):
        return

    def start_session(self):
        welcome_message = """
        *************************************
        *    🙈 Welcome to the arena! 🙉    *
        * What game would you like to play? *
        *************************************

        """        
        game_name = input(welcome_message)

        # if game not imported print no game message
        # else 
        # check max players for game
        
        players_message = """
        How many players today?
        
        \033[1m          1       2  \033[0m

        """

        num_players = input(players_message)

        # start the game
        return
