# code that will continuously ask the user for a letter and validate it.

word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
print (word_list)

from opcode import hasjabs
import random
from re import S
from string import ascii_lowercase 

## choose a random word 

word = random.choice(word_list)
print(word)

# code that will continuously ask the user for a letter and validate it.

while True:
    guess = input ("guess a letter")
    if len(guess) ==1 and guess in ascii_lowercase: # checks that code is a single alphabetical character 
        break
    else :
        print ("Invalid letter. Please, enter a single alphabetical character.")
        
# Checks if the letter guessed by the user is in the secret word that was randomly chosen by the computer. 

if guess in word:  # if statement that checks if the guess is in the word.
    print ("Good guess! {} is in the word.".format(guess))
else:
       print ("Sorry, {} is not in the word. Try again.".format(guess)) # This code will run if the guess is not in the word.

