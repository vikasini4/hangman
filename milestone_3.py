# %%
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
# %%
