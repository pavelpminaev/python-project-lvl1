"""
Module contains game_rule, generate question
and correct answer of brain_gcd game.
"""

from math import gcd
from random import randint

game_rule = 'Find the greatest common divisor of given numbers.'


def answer_generator():
    """Function ask question and return correct_answer"""

    first_randint = randint(1, 100)
    second_randint = randint(1, 100)

    correct_answer = gcd(first_randint, second_randint)
    print(f'Question: {first_randint} {second_randint}')
    return str(correct_answer)
