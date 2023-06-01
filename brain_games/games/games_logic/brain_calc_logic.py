from random import choice
from random import randint
from brain_games.games.games_logic.check_answer import calculate_correct_answer


game_rules = 'What is the result of the expression?'


def game_question():
    question_number_1 = randint(1, 10)
    question_number_2 = randint(1, 10)
    operators = ['+', '-', '*']
    question_operator = choice(operators)
    correct_answer = str(calculate_correct_answer(question_number_1, question_number_2, question_operator))
    task = f'{question_number_1} {question_operator} {question_number_2}'
    return correct_answer, task
