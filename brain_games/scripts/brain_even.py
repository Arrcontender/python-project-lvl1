#!/usr/bin/env python

# import random
# import prompt

# print('Welcome to the Brain Games!')
# name = prompt.string('May I have your name? ')

# print('Hello, ' + name + '!')


# def welcome_user():
#     return name


# def main():
#     welcome_user()


# print('Answer "yes" if the number is even, otherwise answer "no".')


# def game_question():
#     problem = random.randrange(100)
#     print('Question: ' + str(problem))
#     answer = prompt.string('Your answer: ')
#     if answer == 'yes' and problem % 2 == 0:
#         print('Correct!')
#         return True
#     elif answer == 'yes' and problem % 2 == 1:
#         print("'yes' is wrong answer ;(. Correct answer was 'no'.")
#         return False
#     elif answer == 'no' and problem % 2 == 1:
#         print('Correct!')
#         return True
#     elif answer == 'no' and problem % 2 == 0:
#         print("'no' is wrong answer ;(. Correct answer was 'yes'. ")
#         return False
#     else:
#         print("I can't understand you.\nLet's try again, " + name + "!")
#         return False


# result = game_question()
# counter = 1
# while result is True and counter < 3:
#     result = game_question()
#     counter += 1
#     if result is True and counter >= 3:
#         print("Congratulations, " + name + "!")
#     elif result is False:
#         print("Let's try again, " + name + "!")


from brain_games.logic import run_game
from brain_games.games import even

def main():
    return run_game(even)

if __name__ == '__main__':
    main()
