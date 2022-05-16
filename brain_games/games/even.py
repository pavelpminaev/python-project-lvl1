"""
Module contains GAME_RULE, generate question
and correct answer of brain_even game.
"""

from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    """Function generate question and correct_answer"""

    random_num = randint(1, 100)

    question = 'Question: ' + str(random_num)
    correct_answer = 'yes' if random_num % 2 == 0 else 'no'

    return question, correct_answer
