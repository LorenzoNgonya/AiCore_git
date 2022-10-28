
# In this milestone I will use the Object Oriented Programming to develop the whole Hangman game
word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
#print (word_list)



from os import remove
import random
from string import ascii_lowercase

class Hangman:
#      __init__ method to initialise the attributes of the class. Word_list and num_lives as parameters.
    def __init__(self, word_list, num_lives):

# Initialises the following attributes:
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = self.num_lives=5
        self.word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
        self.list_of_guesses = []
    
# check_guess method that will ask the user to guess a letter and another method that will check if the guess is in the word.
    def check_guess_method(self, guess):
        guess = guess.lower()
        if guess in self.word:
    
            print (f"Good guess! {guess} is in the word.")
            for indx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[indx] = letter
            print(self.word_guessed)
            
            if guess in self.num_letters:
                self.num_letters.remove(guess)
            
        else:
            self.num_lives = self.num_lives - 1
            print (f"Sorry, {guess} is not in the word.")
            print (f"You have {self.num_lives} lives left.")
    
        self.list_of_guesses.append(guess)
    
    def ask_for_input (self):
        while True:
            guess = input ("guess a letter ")
            if guess not in ascii_lowercase:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                    print ("You already tried that letter!")
            else :
                self.check_guess_method(guess)
                self.list_of_guesses.append(guess)
                break    
       

#Create a function that will run all the code to run the game as expected
def play_game(word_list):
    game = Hangman (word_list,num_lives=5)
    while True:
        
        if game.num_lives == 0:
            print ("You lost!")
        if len(game.num_letters) >= 1:
            game.ask_for_input()
        else:
            if len(game.num_letters) == 0 and game.num_lives >= 1:
                print ("Congratulations You Won")
                break
           

play_game(word_list)

