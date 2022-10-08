# %%
import random


class Game():
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
    

        if guess in self.word:
            print("Good guess!", guess, "is in the word")
            self.word_guessed.extend(guess)

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
            if guess.isnumeric():
                print("You have entered a number. Please enter a letter.")
            elif guess in self.list_of_guesses :
                print("You already tried that letter!")
            else :
             self.check_guess(guess)
             break

def play_game():
    word_list = ["apple", "banana", "pear", "cherry", "strawberry"]
    game = Game(word_list = word_list,num_lives = 5) 
    
    while True :
     if game.num_lives == 0:
            print("You lost")
            break
           
     elif game.num_letters > 0:
            game.ask_for_input()

     elif game.num_lives  !=0 and game.num_letters==0:
            print("Congratulations! You won the game.")
            break
   

play_game()






g# %%

# %%
