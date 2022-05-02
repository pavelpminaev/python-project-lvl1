"""
Module contains game_rule, generate question
and correct answer of brain_progression game.
"""

from random import randint

game_rule = 'What number is missing in the progression?'


def progression_maker():
    """Function make and return random arithmetic progression"""

    progression = []
    count_num_in_progression = 10
    first_num_in_progression = randint(1, 100)
    diff_progress = randint(1, 10)

    for i in range(0, count_num_in_progression):
        progression.append(first_num_in_progression)
        first_num_in_progression += diff_progress
    return progression


def answer_generator():
    """Function ask question and return correct_answer"""

    progression = progression_maker()
    index_for_del = randint(0, 9)

    correct_answer = progression[index_for_del]
    progression[index_for_del] = '..'
    clean_list = str(progression).strip('[]').replace(",", '').replace("'", '')
    print('Question: ' + str(clean_list))
    return str(correct_answer)
