"""Engine for brain games."""
import prompt


def start(game):
    """Start any Brain  Game."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.game_rule)
    index = 0
    while index <= 2:
        correct_answer = game.answer_generator()
        player_answer = prompt.string('Your answer: ')
        if correct_answer == player_answer:
            print('Correct!')
            index = index + 1
        else:
            print(
                f"'{player_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
    print(f'Congratulations, {user_name}!')
