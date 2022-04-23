"""Docstr for you."""

import prompt
import brain_games.games.even


def start(game):
    """Game Brain even."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(game.game_rule)
    index = 0
    while index <= 2:
        correct_answer = game.answer_generator()
        player_answer = prompt.string('Your answer: ')
        if correct_answer == player_answer:
            print('Correct!')
            index = index + 1
        else:
            print(player_answer + ' is wrong answer ;(. Correct answer was ' + correct_answer)
            print("Let's try again, {0}!".format(user_name))
    print('Congratulations, {0}!'.format(user_name))


start(brain_games.games.even)
