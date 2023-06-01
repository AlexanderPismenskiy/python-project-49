#!/usr/bin/env python3


from brain_games import games_engine
from brain_games.games.games_logic import brain_calc_logic


def main():
    games_engine.engine(brain_calc_logic)


if __name__ == '__main__':
    main()
