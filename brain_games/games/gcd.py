#!/usr/bin/env python

import random

START = 'Find the greatest common divisor of given numbers.'


def game_question():
    x = random.randint(1, 50)
    y = random.randint(1, 50)

    def gcd(a, b):
        while a != b:
            if a > b:
                a = a - b
            elif b > a:
                b = b - a
        return a

    problem = x, y
    result = str(gcd(x, y))

    return problem, result
