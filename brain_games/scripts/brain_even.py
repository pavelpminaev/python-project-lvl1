#!/usr/bin/env python3

"""Docstr for you."""
import random
import prompt


def main():
    """Game Brain even."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index <= 2:
        random_num = random.randint(1, 100)
        print('Question: ' + str(random_num))
        swr = prompt.string('Your answer: ')
        if random_num % 2 == 0:
            true_swr = 'yes'
        else:
            true_swr = 'no'
        if swr == true_swr:
            print('Correct!')
            index = index + 1
        else:
            print(swr + ' is wrong answer ;(. Correct answer was ' + true_swr)
            print("Let's try again, {0}!".format(user_name))
    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
