"""Welcome module, for import to brain_game.py."""
import prompt


def welcome_user():
    """Qwestion name and welcome."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
