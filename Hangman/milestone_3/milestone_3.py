# In this milestone I will use the Object Oriented Programming to develop the whole Hangman game.

# %%

word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
print (word_list)

from opcode import hasjabs
import random
from re import S, X
from string import ascii_lowercase 

word = random.choice(word_list)
print(word)
## choose a random word 
guess = input ("guess a letter")

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [f'',len(word)]
        self.num_letters = word.__sizeof__
        self.num_lives = num_lives
        self.word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
        self.list_of_guesses = [len(guess)]

        def check_guess_method(self):
            if len(guess) ==1 and guess in ascii_lowercase:
                print ("Good guess! {} is in the word.".format(guess))

        def ask_for_input_method(self):
            while True:
                guess = input ("guess a letter")
                if guess not in ascii_lowercase:
                    print ("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in {self.list_of_guesses}:
                        print ("You already tried that letter!")
                else :
                    check_guess_method(guess)
                    {self.list_of_guesses} .append(guess)

