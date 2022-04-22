#!/usr/bin/env python

import random

START = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question():
    problem = random.randint(1, 100)
    result = 'yes' if is_even(problem) else 'no'

    return problem, result


def is_even(number):
    return number % 2 == 0
