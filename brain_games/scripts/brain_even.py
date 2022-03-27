#!/usr/bin/env python3
"""Script for welcome player."""


import prompt


def main():
    """Welcome def."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    main()

