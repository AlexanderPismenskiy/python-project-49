#!/usr/bin/env python3


from brain_games.games.games_logic.brain_calc_logic import calc_answers
from brain_games.games.games_logic.games_rules import welcome_user



def main():
    print("Welcome to the Brain Games!")
    calc_answers()


if __name__ == '__main__':
    main()