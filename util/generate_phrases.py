import random

class RandomPhraseGenerator:
    def __init__(self, combination_length=5):
        self.word_list = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon", "mango",
        "nectarine", "orange", "papaya", "quince", "raspberry",
        "strawberry", "tangerine", "ugli", "vanilla", "watermelon",
        "xigua", "yellowfruit", "zucchini", "apricot", "blueberry",
        "cantaloupe", "dragonfruit", "eggplant", "feijoa", "guava",
        "huckleberry", "indianfig", "jackfruit", "kumquat", "lime",
        "mulberry", "nectar", "olive", "peach", "plum", "pineapple",
        "rhubarb", "starfruit", "tamarind", "ugli", "violet", "wintermelon",
        "yam", "zest", "avocado", "blackberry", "clementine", "durian",
        "elderflower", "fig", "grapefruit", "honeyberry", "imbe", "jambul",
        "kiwifruit", "longan", "mandarin", "nutmeg", "oroblanco", "pitaya",
        "quandong", "rosehip", "soursop", "tangelo", "ugli", "voavanga",
        "wolfberry", "yangmei", "ziziphus", "acai", "bilberry", "camu",
        "damson", "emblica", "fingerlime", "grumichama", "hackberry", "ilama",
        "jabuticaba", "kapok", "lucuma", "mangosteen", "nance", "pawpaw",
        "quenepa", "rambutan", "sapodilla", "tamarillo", "tomato", "ugni", "velvetapple",
        "whitecurrant", "yangmei", "zigzagvine"
        ]
        self.combination_length = combination_length

    def generate_random_phrase(self):
        words = random.sample(self.word_list, self.combination_length)
        return ''.join(words)
