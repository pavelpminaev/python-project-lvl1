"""
Module contains GAME_RULE, generate question
and correct answer of brain_calc game.
"""

from operator import add, sub, mul
from random import randint, choice

GAME_RULE = 'What is the result of the expression?'


def answer_generator():
    """Function ask question and return correct_answer"""

    dict_operators = {
        '+': add,
        '-': sub,
        '*': mul
    }
    first_randint = randint(1, 10)
    second_randint = randint(1, 10)
    operator = choice(list(dict_operators.keys()))

    print(f'Question: {first_randint} {operator} {second_randint}')
    correct_answer = dict_operators[operator](first_randint, second_randint)
    return str(correct_answer)
