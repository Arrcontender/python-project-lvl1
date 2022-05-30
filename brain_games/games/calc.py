#!/usr/bin/env python

import random

START = 'What is the result of the expression?'


def game_question():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.choice('+-*')

    def math_result(a, b, c):
        if c == '+':
            v = a + b
            return v
        elif c == '-':
            v = a - b
            return v
        else:
            v = a * b
            return v
    problem = "{0} {1} {2}".format(str(x), str(z), str(y))
    result = str(math_result(x, y, z))

    return problem, result
