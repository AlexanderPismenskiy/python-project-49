import prompt
from random import randint
from brain_games.cli import welcome_user


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    

def check_answer():
    if True:
        return 'yes'
    else:
        return 'no'
        

def player_answer():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_attempts = 3
    
    for _ in range(number_of_attempts):
        
        question_number = randint(1,450)
        print(f'Question: {question_number}')
        answer = prompt.string('Your answer: ')
        
        if is_even(question_number) == True and answer == 'yes':
            return('Correct!')
        if is_even(question_number) == False and answer == 'no':
            return('Correct!')
        if is_even(question_number) == True and answer == 'no':
            return(f''''no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name} !''')
            break
        if is_even(question_number) == False and answer == 'yes':
            return(f''''yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name} !''')
            break
        print(f'''Congratulations, {name}''')
