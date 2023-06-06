import prompt

NUMBER_OF_ATTEMPTS = 3   # количесвто раундов игры


def start_game(game):
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    print(game.GAME_RULE)
    for _ in range(NUMBER_OF_ATTEMPTS):
        correct_answer, question = game.get_game()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')
        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'."
                  f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')
