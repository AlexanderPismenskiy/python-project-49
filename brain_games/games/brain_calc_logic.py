from random import choice
from random import randint
from brain_games.games.check_answer import calc_answer


GAME_RULE = 'What is the result of the expression?'


def game_question():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    operators = ['+', '-', '*']
    question_operator = choice(operators)
    correct_answer = str(calc_answer(number_1, number_2, question_operator))
    task = f'{number_1} {question_operator} {number_2}'
    return correct_answer, task
