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
    
# Milestone 2    

Creation of two functions to run the checks.

• check_guess(): This function will take the guessed letter as an argument and check if the letter is in the word.
• ask_for_input(): If the guessed letter is valid, the function will check afterwards whether the character occurs in the word. Otherwise, it will repeat the loop until getting the valid input.

# Create functions  
import milestone_2 as m2

def check_guess(guess):
    guess=guess.lower()
    if guess in m2.random_word:
     print('Good Guess!', guess, 'is in the word')
    else:
     print('Sorry,', guess, 'is not in the word. Try again.')

def ask_for_input():
    while True :
        guess = input("guess a letter")
        if guess.isalpha() and len(guess) ==1:
            break
        else :
         print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()

# Milestone 3

Creation of game class and methods for running the checks.

• check_guess() method: This method checks if the letter is present in the word.
• ask_for_input() method: This method creates a list of single alphabetical characters with the user input.

import random


class Hangman():
    def __init__(self,word_list,num_lives):

     self.word_list = word_list
     self.num_lives = num_lives

     self.word = random.choice(word_list)
     self.word_guessed = [",", ",", ",", ",", ","]
     self.num_letters = int(len(set(self.word) - set(self.word_guessed)))
     self.num_lives = 5
     self.word_list = word_list
     self.list_of_guesses =[]
    
    def check_guess(self,guess):
        guess = guess.lower()
        self.word_guessed.extend(guess)

        if guess in self.word:
            print("Good guess!", guess, "is in the word")

            for i, letter in enumerate(self.word): 
                if letter == guess:
                    self.word_guessed[i] = guess 
            self.num_letters -= 1
        else :
            self.num_lives -= 1
            print("Sorry,", guess, "is not in the word. Try again.")
            print("You have", self.num_lives,"lives left." )

        self.list_of_guesses.append(guess)


    def ask_for_input(self):
        while True :
            guess = input("Enter a single letter")
            if not guess.isalpha() and not len(guess) == 1:
                print("Invalid letter. Please, enter a single alphabetic character.")
            elif guess in self.list_of_guesses :
                print("You already tried that letter!")
            else :
             self.check_guess(guess)
             break




