import json
import random


class Wordlist():
    def __init__(self):
        self.words = {}

    def create_wordlist(self, path):  # convert a txt file to a python dictionary
        with open(path, 'r', encoding='UTF-8') as f:
            contents = f.readlines()
        result = {}
        for eachline in contents:
            eachline = eachline.rstrip()
            if not len(eachline) == 1:
                res = eachline.split(' ')
                result[res[0]] = res[1:]

        self.words = result

    def save(self, path):  # convert the python dictionary to a json file
        file = json.dumps(self.words)
        with open(path, 'w') as f:
            f.writelines(file)

    def read(self, path):  # read a json file and save it as a dictionary
        with open(path) as json_file:
            self.add(json.load(json_file))

    def add(self, w):  # add words to self.words
        # print(w)
        for each in w:
            # print(each)
            self.words[each] = w[each]

    def delete(self, word):
        return self.words.pop(word)

    def get(self, key):
        return self.words[key]

    def getall(self):
        return self.words

    def set(self, words):
        self.words = words


class WordlistWithPosition(Wordlist):
    def __init__(self, prev_words_list, cur_words):
        Wordlist.__init__(self)
        self.add(prev_words_list)
        self.add(cur_words)
        self.keys = list(self.words.keys())
        self.words = self.shuffle()
        self.pos = 0
        self.curr_word = self.keys[self.pos]

    def shuffle(self):
        random.shuffle(self.keys)
        new_dict = {}
        for key in self.keys:
            new_dict[key] = self.words[key]
        return new_dict

    def next(self):

        if self.pos >= len(self.keys) - 1:
            return self.curr_word
        else:
            self.pos += 1
            self.curr_word = self.keys[self.pos]

            return self.curr_word

    def previous(self):
        if self.pos <= 0:
            self.curr_word = self.keys[self.pos]
            return self.curr_word
        else:
            self.pos -= 1
            self.curr_word = self.keys[self.pos]
            return self.curr_word

    def translate(self):
        if not self.curr_word in self.words:

            self.curr_word = self.keys[self.pos]
            return self.curr_word
        else:
            word = ''
            for each in self.words[self.keys[self.pos]][1:]:
                word += each
            self.curr_word = word
            return self.curr_word



