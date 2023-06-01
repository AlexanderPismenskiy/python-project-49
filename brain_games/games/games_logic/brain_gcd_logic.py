import math
from random import randint


game_rules = 'Find the greatest common divisor of given numbers.'

def game_question():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    task = f'{number_1} {number_2}'
    correct_answer = str(math.gcd(number_1, number_2))
    return correct_answer, task
