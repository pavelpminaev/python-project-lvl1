"""
Module contains GAME_RULE, generate question
and correct answer of brain_progression game.
"""

from random import randint
from copy import copy

GAME_RULE = 'What number is missing in the progression?'


def generate_progression(
                        count_num_progression,
                        first_num_progression,
                        diff_num_progression
                        ):
    """Function make and return arithmetic progression"""

    progression = []

    for _ in range(0, count_num_progression):
        progression.append(first_num_progression)
        first_num_progression += diff_num_progression
    return progression


def generate_question_answer():
    """Function generate question and correct_answer"""

    progression = generate_progression(10, randint(1, 100), randint(1, 10))
    index_for_del = randint(0, 9)

    question = copy(progression)
    question[index_for_del] = '..'
    question = str(question).strip('[]').replace(",", '').replace("'", '')

    question = f'Question: {question}'
    correct_answer = progression[index_for_del]

    return question, str(correct_answer)
