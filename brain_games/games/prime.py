"""
Module contains GAME_RULE, generate question
and correct answer of brain_prime game.
"""

from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Function defines prime numbers"""

    if number < 2:
        return False
    else:
        divider = 2
        while divider <= number / 2:
            if number % divider == 0:
                return False
            divider += 1
        return True


def generate_question_answer():
    """Function generate question and correct_answer"""

    number = randint(0, 100)

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = str(number)

    return question, correct_answer
