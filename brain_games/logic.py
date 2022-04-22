#!/usr/bin/env python

import prompt
from brain_games.games import even
from brain_games.games.even import game_question

def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(even.START)
    number_of_round = 0
    rounds_to_win = 3
    while number_of_round < rounds_to_win:
        problem, result = game_question()
        print(f'Question: {problem}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == result:
            print('Correct!')
            number_of_round += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')