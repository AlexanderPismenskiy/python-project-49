from random import randint
from random import choice


game_rules = 'What number is missing in the progression?'


def game_question():
    start = randint(1, 10)
    stop = randint(20, 50)
    step = randint(2, 7)
    progression = []
    for i in range(start, stop, step):
        progression.append(i)
    hiden_number = (choice(progression))
    hiden_index = progression.index(hiden_number)
    correct_answer = str(hiden_number)
    progression[hiden_index] = '...'
    task = progression
    return correct_answer, task
