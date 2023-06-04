from random import randint
from brain_games.games.check_answer import check_answer


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    task = randint(1, 999)
    even_number = is_even(task)
    correct_answer = check_answer(even_number)
    return correct_answer, task
