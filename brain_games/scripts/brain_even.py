#!/usr/bin/env python3


from brain_games.games_engine import start_game
from brain_games.games import brain_even_logic


def main():
    start_game(brain_even_logic)


if __name__ == '__main__':
    main()
