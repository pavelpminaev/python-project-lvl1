"""Welcome module, for import to brain_games.py."""

import prompt


def welcome_user():
    """Question name and welcome."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
