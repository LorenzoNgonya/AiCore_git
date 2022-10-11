# code that will continuously ask the user for a letter and validate it.

from string import ascii_lowercase


while True:
    guess = input ("guess a letter")
    if len(guess) ==1 and guess in ascii_lowercase:
        break
    else :
        print ("Invalid letter. Please, enter a single alphabetical character.")