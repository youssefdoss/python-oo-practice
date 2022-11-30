from random import choice

class WordFinder:
    '''Word Finder: finds random words from a dictionary.'''

    def __init__(self, file):
        '''Creates WordFinder given a file'''
        self.file = file
        self.words = self.store_words()
        self.print_word_count()
    
    def __repr__(self):
        return f'<WordFinder file={self.file} words={self.words}>'

    def store_words(self):
        '''Stores each word of given file and creates a list of those words'''
        words = []

        with open(self.file) as file:
            for word in file:
                # strip() will take out new line characters and things of that sort
                word = word.replace('\n', '')
                words.append(word)

        return words

    def print_word_count(self):
        '''Prints number of words read in file'''
        print(f'{len(self.words)} words read')

    def random(self):
        '''Selects a random word from the words list and returns it'''
        return choice(self.words)


class RandomWordFinder(WordFinder):
    '''Inherits from WordFinder. Finds random words from given file but excludes comments'''

    # def __init__(self, file):
    #     '''Create RandomWordFinder given a file'''
    #     self.file = file
    #     self.words = self.store_words()
    #     super().print_word_count()
    
    def __repr__(self):
        return super().__repr__().replace('WordFinder', 'RandomWordFinder')

    def store_words(self):
        '''Stores each word of a given file in words, excluding comments'''
        words = super().store_words()

        return [word for word in words if not (word == '' or word.startswith('#'))]

