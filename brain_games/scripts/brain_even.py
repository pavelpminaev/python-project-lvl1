#!/usr/bin/env python3


import prompt
import random


def main():
    """Game Brain even."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 2:
        random_num = random.randint(1, 100) 
        print('Question: ' + str(random_num))
        answer = prompt.string('Your answer: ')
        if random_num % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        if answer == true_answer:
            print('Correct!')
            i = i + 1
        else:
            print(answer + ' is wrong answer ;(. Correct answer was ' + true_answer)
            print("Let's try again, {0}!".format(user_name))
    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
