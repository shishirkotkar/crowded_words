import json
from nltk.corpus import stopwords
from collections import Counter
import pandas

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
        if word.lower() in self.stop_words:
            return True
        return False

    def is_bad_word(self, word=None):
        bad_words = ['also']
        if word.lower() in bad_words:
            return True
        return False

    def get_words(self):
        filtered_words = []
        words = self.process_string()
        for word in words:
            try:
                if any([self.is_stop_word(word),
                        self.is_alpha_numeric(word=word),
                        self.word_has_special_characters(word=word),
                        self.is_bad_word(word=word)]):
                    continue
                else:
                    filtered_words.append(word)
            except:
                continue
        return filtered_words


class DataAdapter(object):

    def __init__(self, data_processor=None):
        self.data_processor = data_processor

    def build_data(self):
        words = self.data_processor.get_words()
        count = Counter(words)
        output = []
        for word, freq in count.items():
            if freq >= 5:
                output.append({'text': word, 'size': freq})
        return output

    def top_100_words(self, data=None):
        df = pandas.DataFrame(data)
        df = df.sort('size', ascending=False)
        df = df.head(n=100)
        return df.T.to_dict().values()

    def get_json(self):
        data = self.build_data()
        top_100 = self.top_100_words(data=data)
        return json.dumps({'frequency_list': top_100})
