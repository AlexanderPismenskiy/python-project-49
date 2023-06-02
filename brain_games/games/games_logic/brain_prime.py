from random import randint
from brain_games.games.games_logic.check_answer import check_answer

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def game_question():
    task = randint(1, 100)
    prime_number = is_prime(task)
    correct_answer = check_answer(prime_number)
    return correct_answer, task
