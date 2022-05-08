"""
Module contains GAME_RULE, generate question
and correct answer of brain_even game.
"""

from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def answer_generator():
    """Function ask question and return correct_answer"""

    random_num = randint(1, 100)

    print('Question: ' + str(random_num))
    correct_answer = 'yes' if random_num % 2 == 0 else 'no'
    return correct_answer
