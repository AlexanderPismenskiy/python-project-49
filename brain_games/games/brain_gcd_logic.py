import math
from random import randint


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    question = f'{number_1} {number_2}'
    correct_answer = str(math.gcd(number_1, number_2))
    return correct_answer, question
