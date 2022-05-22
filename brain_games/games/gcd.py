"""
Module contains GAME_RULE, generate question
and correct answer of brain_gcd game.
"""

from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def gcd(first_num, second_num):
    while second_num:
        first_num, second_num = second_num, first_num % second_num
    return first_num


def generate_question_answer():
    """Function generate question and correct_answer"""

    first_num = randint(1, 100)
    second_num = randint(1, 100)

    question = f'{first_num} {second_num}'
    correct_answer = gcd(first_num, second_num)

    return question, str(correct_answer)
