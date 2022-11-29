from random import choice

class WordFinder:
    '''Word Finder: finds random words from a dictionary.'''

    def __init__(self, file):
        '''Creates wordfinder given a file'''
        self.file = open(file)
        self.words = self.read_word_by_word()

    
    def read_word_by_word(self):
        '''Prints each word of given file and creates a list of those words'''
        words = []

        with self.file as file:
            for line in file:
                for word in line.split():

                    words.append(word)

        print(f'{len(words)} words read')
        return words

    def random(self):
        '''Selects a random word from the words list and returns it'''
        return choice(self.words)
