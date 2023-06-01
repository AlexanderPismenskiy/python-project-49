#!/usr/bin/env python3


import brain_games
from brain_games.games.games_logic.cli import welcome_user


def start_game(module):
    print("Welcome to the Brain Games!")


def main():
    start_game(brain_games)
    welcome_user()


if __name__ == '__main__':
    main()
