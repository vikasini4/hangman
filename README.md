# Milestone 1
Creation of the variables of the game.
In order to complete the Hangman Project, you will need to create variables of the game with basic Python commands.

import random

# List of words

word_list = ('apple', 'strawberry', 'kiwi', 'cherry', 'banana')
print(word_list)

# Random word from the list

random.choice(word_list)
word = random.choice(word_list)
print(word)

# Enter an input

input('enter a single letter')
guess = input('enter a single letter')
print(guess)

# Check the input is a single character

a = input('Enter an alphabet')
x = len(a)
if x == 1:
    print('Good Guess')
else:
    print('Oops! That is not a valid input.')
