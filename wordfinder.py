from random import choice

class WordFinder:
    '''Word Finder: finds random words from a dictionary.'''

    def __init__(self, file):
        '''Creates WordFinder given a file'''
        self.file = file
        self.words = self.store_words()


    def store_words(self):
        '''Stores each word of given file and creates a list of those words'''
        words = []

        with open(self.file) as file:
            for line in file:
                for word in line.split():

                    words.append(word)

        print(f'{len(words)} words read')
        return words

    def random(self):
        '''Selects a random word from the words list and returns it'''
        return choice(self.words)


class RandomWordFinder(WordFinder):
    '''Inherits from WordFinder. Finds random words from given file but excludes comments'''

    def __init__(self, file):
        '''Create RandomWordFinder given a file'''
        self.file = file
        self.words = self.store_words_ignoring_comments()

    def store_words_ignoring_comments(self):
        '''Stores each word of a given file in words, excluding comments'''
        words = []

        with open(self.file) as file:
            for line in file:
                if not line[0] == "#":
                    for word in line.split():

                        words.append(word)

        print(f'{len(words)} words read')
        return words


