#!/usr/bin/env python

import random

START = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_question():
    number = random.randint(2, 100)
    result = 'yes'
    for i in range(2, number):
        if number % i == 0:
            result = 'no'
    problem = number
    return problem, result
