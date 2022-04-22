#!/usr/bin/env python

import random

START = 'What is the result of the expression?'


def game_question():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.choice('+-*')


    def math_problem(a, b, c):
        if c == '+':
            q = str(a) + ' + ' + str(b)
            return q
        elif c == '-':
            q = str(a) + ' - ' + str(b)
            return q
        else:
            q = str(a) + ' * ' + str(b)
            return q


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


    problem = (math_problem(x, y, z))
    result = str(math_result(x, y, z))

    return problem, result
