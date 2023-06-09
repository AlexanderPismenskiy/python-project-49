from random import randint
from random import choice


GAME_RULE = 'What number is missing in the progression?'


def make_progression():
    first_number, difference = randint(1, 30), randint(1, 10)
    progression_length = randint(5, 10)
    progression = []
    for i in range(progression_length):
        first_number += difference
        progression.append(first_number)
    return progression


def get_game():
    progression = make_progression()
    hiden_number = choice(progression)
    hiden_index = progression.index(hiden_number)
    correct_answer = str(hiden_number)
    progression[hiden_index] = ".."
    question = ' '.join(map(str, progression))
    return correct_answer, question
