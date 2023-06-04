from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    task = randint(1, 999)
    if is_even(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, task
