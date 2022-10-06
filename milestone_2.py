# %%
while True :
   guess = input("guess a letter")
   if guess.isalpha() and len(guess) ==1:
     break
   else :
    print("Invalid letter. Please, enter a single alphabetical character.")

# %%
import random

words = ["apple", "british", "food", "computer", "book", "programming"]
random_word = random.choice(words)
guess = str(input("Guess a letter"))

if guess in random_word:             
   print('Good Guess!', guess, 'is in the word')
else:
   print('Sorry,', guess, 'is not in the word. Try again.')
        

# %%
