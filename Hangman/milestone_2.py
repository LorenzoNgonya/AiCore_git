# this will allow the code to chose a word randomly

import random

from milestone_1 import word_list

def word ():
    word = random.choice(word_list)
    
    print(word)