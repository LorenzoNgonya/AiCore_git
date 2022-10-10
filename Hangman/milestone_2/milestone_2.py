# code that will continuously ask the user for a letter and validate it.

word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
print (word_list)

from opcode import hasjabs
import random
from string import ascii_lowercase

## choose a random word 

word = random.choice(word_list)
print(word)

### user input 

guess = input("guess a letter")

print(guess)

letter = guess

while letter == True:
    if len(guess) ==1:
     if guess in ascii_lowercase:
        break
if len(guess) >1:
    if guess not in ascii_lowercase:
        print("Invalid letter. Please, enter a single alphabetical character.")

   