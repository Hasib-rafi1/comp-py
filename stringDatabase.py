#Python class for reading words from text file and store in a list.
"""
This is the "stringDatabase" module.
Python class for reading words from text file and store in a list.
"""
import random
class stringDatabase:
    # reading file
    text_file = open("four_letters.txt", "r")
    #spliting and storing in a list
    words = text_file.read().split(' ')
    def __init__(self):
        self.obja = ""

    def get_random_word(self):
        """
        Python random method to choose random word
        """
        return random.choice(self.words)
