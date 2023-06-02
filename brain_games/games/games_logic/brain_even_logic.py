from random import randint
from brain_games.games.games_logic.check_answer import check_answer


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_question():
    task = randint(1, 999)
    even_number = is_even(task)
    correct_answer = check_answer(even_number)
    return correct_answer, task
