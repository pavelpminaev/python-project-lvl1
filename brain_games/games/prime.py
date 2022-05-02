from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def answer_generator():
    """Function ask question and return correct_answer"""

    number = randint(0, 100)
    print(f'Question: {number}')

    if number < 2:
        return 'no'
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1
    return 'yes'