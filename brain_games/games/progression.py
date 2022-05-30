#!/usr/bin/env python

import random

START = 'What number is missing in the progression?'

def game_question():
    pr_ssn_start = random.randint(0, 100)
    pr_ssn_len = random.randint(5, 10)
    pr_ssn_step = random.randint(2, 50)
    pr_ssn_hide = random.randint(0, pr_ssn_len - 1)
    pr_ssn = []
    counter = pr_ssn_len
    while counter > 0:
        pr_ssn.append(str(pr_ssn_start))
        pr_ssn_start = pr_ssn_start + pr_ssn_step
        counter -= 1
    hidden_num = pr_ssn[pr_ssn_hide]
    pr_ssn.pop(pr_ssn_hide)
    pr_ssn.insert(pr_ssn_hide, '..')
    result = ' '.join(pr_ssn)
    problem = hidden_num
    return result, problem

# def game_question():
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
