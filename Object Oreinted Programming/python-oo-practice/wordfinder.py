"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Class used to pick random words from a dictionary"""

    def __init__(self, path):
        """This opens our dictionary and prints back how many words where read"""
        dict_file = open(path)
        self.words = self.aprse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Makes dict_file into a list of words"""
        return [w.strip() for w in dict_file]

    def random(self):
        """Returns random word"""
        return random.choice(self.words)



    class SpecialWordFinder(WordFinder):
        def parse(self, dict_file):
            """Takes dict_file, makes it a list of words but skips comments/blanks"""

            return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')]