#!/usr/bin/env python3

from brain_games.games_engine import start_game
from brain_games.games import brain_gcd_logic


def main():
    start_game(brain_gcd_logic)


if __name__ == '__main__':
    main()
