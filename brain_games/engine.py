"""Engine of "brain games" games."""

import prompt

ROUNDS_COUNT = 3


def start(game):
    """Start any game."""

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULE)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_question_answer()
        print(question)
        player_answer = prompt.string('Your answer: ')
        if correct_answer == player_answer:
            print('Correct!')
        else:
            print(
                f"'{player_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            return
    print(f'Congratulations, {user_name}!')
