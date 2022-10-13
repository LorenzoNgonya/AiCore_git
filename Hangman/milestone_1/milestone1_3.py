# this will add user input

word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
print (word_list)

import random
from string import ascii_lowercase

## choose a random word 

word = random.choice(word_list)
print(word)

### user input 

guess = input("guess a letter")


### if statement that checks it's a single letter 

if len(guess) ==1:
    if guess in ascii_lowercase:
        print("Good guess!")
        
else:
    print("Oops! That is not a valid input")