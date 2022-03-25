import datetime
from import_file import Wordlist
import random


# print(datetime.date.today())
# print(datetime.date.today()-datetime.timedelta(100))

class Plan():
    def __init__(self):
        self.today = datetime.date.today()
        self.review_date = [1, 2, 4, 7, 15]
        self.reviews = self.create_plan()
        self.oldwords, self.newwords = self.get_words()

    def create_plan(self):
        result = []
        for date in self.review_date:
            result.append(str(self.today - datetime.timedelta(date)))
        return result

    def get_words(self):
        review_words = Wordlist()  # get old words
        for date in self.reviews:
            try:
                review_words.read('./words/' + date + '.json')
            except:
                pass
        try:
            new_words = Wordlist()
            new_words.read('./words/' + str(self.today) + '.json')
        except FileNotFoundError:
            dic = Wordlist()  # choose new words randomly
            dic.read('./words/CET6.json')
            dic_list = list(dic.words)
            new_words = Wordlist()
            d = {}
            for i in range(15):
                word = random.choice(dic_list)
                translation = dic.delete(word)
                d[word] = translation
            new_words.add(d)
            dic.save('./words/CET6.json')  # delete chosen words from CET4
            new_words.save('./words/' + str(self.today) + '.json')  # save new words

        return review_words.getall(), new_words.getall()

    def get_oldwords(self):
        return self.oldwords

    def get_newwords(self):
        return self.newwords
