import prompt

number_of_attempts = 3   # количесвто раундов игры


def greeting():
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    return player_name


def engine(game):
    player_name = greeting()
    print(game.game_rules)
    winner = True
    for _ in range(number_of_attempts):
        correct_answer, task = game.game_question()
        print(f'Question: {task}')
        player_answer = prompt.string('Your answer: ')
        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. 
Let's try again, {player_name}!""")
            winner = False
            break      
    if winner:
        print(f'Congratulations, {player_name}!')
