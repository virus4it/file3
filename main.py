from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:

            with open(file_name, 'r', encoding='utf-8') as file:

                text = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(char, ' ')

                words = text.split()
                all_words[file_name] = words



        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():

            if word in words:
                positions[file_name] = words.index(word) + 1

        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():

            counts[file_name] = words.count(word)

        return counts



finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))