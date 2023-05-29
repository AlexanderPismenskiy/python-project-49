#!/usr/bin/env python3



from brain_games.brain_even_logic import player_answer
#from brain_games.brain_even_logic import question_number
#from brain_games.brain_even_logic import game_replay
#from brain_games.brain_even_logic import user_name
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    #welcome_user()
    player_answer()
    #print('Answer "yes" if the number is even, otherwise answer "no".')
    


if __name__ == '__main__':
    main()