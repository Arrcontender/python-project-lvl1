#!/usr/bin/env python

import random

START = 'What number is missing in the progression?'


def game_question():
    diff = random.randint(1, 5)
    first = random.randint(1, 5)
    quise = first + (random.randint(0, 9) * diff)
    after_last = first + (10 * diff)
    test_string = ''
    a = ''
    for i in range(first, after_last, diff):
        a = '..' if i == quise else str(i)
        test_string = f'{test_string} {a}'
    result = (f'{test_string}')
    problem = str(quise)
    return result, problem
