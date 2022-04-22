#!/usr/bin/env python

import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.START)
    number_of_round = 0
    rounds_to_win = 3
    while number_of_round < rounds_to_win:
        problem, result = game.game_question()
        print(f'Question: {problem}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == result:
            print('Correct!')
            number_of_round += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
