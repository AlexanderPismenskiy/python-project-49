#!/usr/bin/env python3


from brain_games.brain_calc_logic import calc_answers
from brain_games.games_rules import welcome_user



def main():
    welcome_user()
    calc_answers()


if __name__ == '__main__':
    main()