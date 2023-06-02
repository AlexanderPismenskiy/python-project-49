#!/usr/bin/env python3

from brain_games.games_engine import engine
from brain_games.games.games_logic import brain_prime


def main():
    engine(brain_prime)


if __name__ == '__main__':
    main()
