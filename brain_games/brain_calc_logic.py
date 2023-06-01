from random import choice
from random import randint
import prompt
from brain_games.check_answer import calculate_correct_answer
from brain_games.games_rules import start_game


number_of_attempts = 3 # количество раун



def calc_answers():
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    print('What is the result of the expression?')
    start_game()
    winner = True
    for _ in range(number_of_attempts):
        question_number_1 = randint(1, 10)
        question_number_2 = randint(1, 10)
        operators = ['+', '-', '*' ]
        question_operator = choice(operators)
        print(f'''Question: {question_number_1} {question_operator} {question_number_2}''')
        player_answer = prompt.integer('Your answer: ')
        correct_answer = calculate_correct_answer(question_number_1,question_number_2, question_operator)
        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. 
Let's try again, {player_name}!""")
            winner = False
            break      
    if winner:
        print(f'Congratulations, {player_name}!')