# %%

import random

word_list = ('apple', 'strawberry', 'kiwi', 'cherry', 'banana')
print(word_list)

# %%
random.choice(word_list)
word = random.choice(word_list)
print(word)
# %%
input('enter a single letter')
guess = input('enter a single letter')
print(guess)

# %%
a = input('Enter an alphabet')
x = len(a)
if x == 1:
    print('Good Guess')
else:
    print('Oops! That is not a valid input.')



# %%
