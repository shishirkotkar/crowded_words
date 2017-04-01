from nltk.corpus import stopwords


class DataProcessor(object):

    def __init__(self, input_data=None):
        self.input_data = input_data
        self.stop_words = set(stopwords.words('english'))

    def process_string(self):
        word_list = []
        for row in self.input_data:
            row = row.replace('\n', ' ')
            row = row.replace('\r', ' ')
            row = row.split(" ")
            word_list += row
        return self.fix_punctuations(words=word_list)

    def fix_punctuations(self, words=None):
        words = [w.replace(';', ' ').replace(',', ' ').replace('.', ' ')
                 .replace('!', ' ').replace('(', ' ').replace(')', ' ').strip()
                 for w in words if len(w) > 2]
        return words

    def is_alpha_numeric(self, word=None):
        return False if str(word).isalpha() else True

    def word_has_special_characters(self, word=None):
        if any(ord(char) > 126 for char in word):
            return True
        return False

    def is_stop_word(self, word=None):
        if word in self.stop_words:
            return True
        return False

    def run(self):
        filtered_words = []
        words = self.process_string()
        for word in words:
            try:
                if any([self.is_stop_word(word),
                        self.is_alpha_numeric(word=word),
                        self.word_has_special_characters(word=word)]):
                    continue
                else:
                    filtered_words.append(word)
            except:
                continue
        return filtered_words

