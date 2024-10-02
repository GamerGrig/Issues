class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def info(self):
        print(self.file_names)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                words = file.read().split()
                wordsqq = self.symbol_del(words)
                for i in wordsqq:
                    if file.name not in all_words:
                        all_words[file.name] = []
                        all_words[file.name].append(i.lower())
                    else:
                        all_words[file.name].append(i.lower())
            return all_words

    def find(self, word):
        d = {}
        word = word.lower()
        text = self.get_all_words()
        for key, value in text.items():
            try:
                d[key] = (value.index(word) + 1)
                return d
            except ValueError:
                return 'Такого слова нет'

    def count(self, count_word):
        d_count = {}
        count_word = count_word.lower()
        text = self.get_all_words()
        for key, value in text.items():
            d_count[key] = value.count(count_word)
            return d_count

    def symbol_del(self, list_):
        l = []
        translator = str.maketrans('', '', ",,.=!?;: - ")
        for word in list_:
            clean_word = word.translate(translator)
            l.append(clean_word)
        return l


f1 = 'file1.txt'
f2 = 'file2.txt'

finder1 = WordsFinder(f2)
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
