# %%
import random

class Game():
    ''' a Hangman game that asks the player for a letter and checks if it matches in the word. 
It starts with a default number of lives and a random word from the word list.

Parameters:
   
word_list: list - List of words used in the game
num_lives: int - Number of lives left
    
Attributes:
    
word: str - The word to be guessed picked randomly from the word_list
word_guessed: list - A list of the letters of the word, with '_' for each letter not yet guessed
num_letters: int - The number of unique letters in the word that have not been guessed yet
num_lives: int - The number of lives left
list_of_guesses: list - A list of the letters that have already been guessed
    
Methods:

check_guess(guess): Checks if the letter is in the word.
ask_input(): Asks the user for a letter.

'''

    def __init__(self,word_list,num_lives):

     self.word_list = word_list
     self.num_lives = num_lives
     self.word = random.choice(word_list)
     self.word_guessed = [","] * len(self.word)
     self.num_letters = len(list(set(self.word)))
     self.num_lives = 5
     self.word_list = word_list
     self.list_of_guesses =[]
    
    def check_guess(self,guess):
        """
        Checks if the guessed letter is in the word.
        If it is, it will replace the '_' in the word_guessed list with the guessed letter.
        If it is not, the number of lives will be reduced by 1.

        Parameters:

        guess: str - The guess to be checked

        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess!", guess, "is in the word")
            for i, letter in enumerate(self.word): 
                if letter == guess:
                    self.word_guessed[i] = guess 
            print(self.word_guessed)
            self.num_letters -= 1
        else :
            self.num_lives -= 1 
            print(f"Sorry,", guess, "is not in the word. Try again.")
            print(f"You have", self.num_lives,"lives left." )
       
    def ask_for_input(self):
        """
        Asks the user for a guess and checks:
        1. If the guess has already been tried.
        2.If the character is a single alphabetic character.
        If both passes, then it will call the check_guess method.

        """
        while True :
            guess = input("Enter a single letter\t") 
        
            if len(guess) != 1:
                print(f"Invalid input. Please, enter a single alphabetic character.")
            elif guess.isnumeric():
                print(f"You have entered a number. Please enter a letter.")
            elif guess in self.list_of_guesses :
                print(f"You already tried that letter!")
            else :
                break
        self.list_of_guesses.append(guess)
        self.check_guess(guess) 

def play_game():
    word_list = ["apple", "banana", "pear", "cherry", "strawberry"]
    game = Game(word_list = word_list,num_lives = 5) 
    
    while True:
        if game.num_lives > 0:
         game.ask_for_input()
         print(f"Guessed letters so far: {', '.join(game.list_of_guesses)}\n")
        
        if game.num_lives == 0:
             print(f"You lost")
             break
           
        elif game.num_lives  !=0 and game.num_letters==0:
             print(f"Congratulations! You won the game.")
             break

play_game()




# %%

# %%
