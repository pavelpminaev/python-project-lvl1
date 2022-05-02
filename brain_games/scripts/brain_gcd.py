#!/usr/bin/env python3
"""Script of brain_calc game."""

from brain_games.engine import start
from brain_games.games import gcd


def main():
    start(gcd)


if __name__ == '__main__':
    main()
