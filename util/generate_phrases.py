import random
from util.word_list import word_list

class RandomPhraseGenerator:
    def __init__(self, combination_length=5):
        self.word_list = word_list
        self.combination_length = combination_length

    def generate_random_phrase(self):
        words = random.choices(self.word_list, k=self.combination_length)
        return ''.join(words)
