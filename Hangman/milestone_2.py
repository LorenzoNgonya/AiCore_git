# this will allow the code to chose a word randomly

import _random

from word_list import random

from milestone_1 import word_list

def word(word_list):
    word =random.choice(word_list)
    
print(word)

