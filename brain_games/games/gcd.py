"""
Module contains GAME_RULE, generate question
and correct answer of brain_gcd game.
"""

from math import gcd
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    """Function generate question and correct_answer"""

    first_randint = randint(1, 100)
    second_randint = randint(1, 100)

    question = f'Question: {first_randint} {second_randint}'
    correct_answer = gcd(first_randint, second_randint)

    return question, correct_answer
