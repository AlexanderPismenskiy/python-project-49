import prompt
from random import randint
from brain_games.check_answer import check_answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def player_answers():
    number_of_attempts = 3
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    winner = True
    for _ in range(number_of_attempts):
        question_number = randint(1, 999)
        print(f'Question: {question_number}')
        player_answer = prompt.string('Your answer: ')
        even_number = is_even(question_number)
        correct_answer = check_answer(even_number)
        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. 
Let's try again, {player_name}!""")
            winner = False
            break
    if winner:
        print(f'Congratulations, {player_name}!')
