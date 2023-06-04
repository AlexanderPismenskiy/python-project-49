import prompt

number_of_attempts = 3   # количесвто раундов игры


def greeting():
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    return player_name


def engine(game):
    player_name = greeting()
    print(game.GAME_RULE)
    winner = True
    for _ in range(number_of_attempts):
        correct_answer, task = game.get_game()
        print(f'Question: {task}')
        player_answer = prompt.string('Your answer: ')
        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{player_answer}' is wrong answer ;(."""
                  f"""Correct answer was '{correct_answer}.'"""
                  f"""Let's try again, {player_name}!""")
            winner = False
            break
        if winner:
            print(f'Congratulations, {player_name}!')
