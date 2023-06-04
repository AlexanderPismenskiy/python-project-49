from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return True
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def get_game():
    task = randint(2, 100)
    if is_prime(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, task
