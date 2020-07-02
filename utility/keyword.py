import re


class Keyword:
    # keywords = []
    def __init__(self, keywords):
        self.__keywords = keywords

    def set_keywords(self, keywords):
        self.__keywords = keywords

    def get_keywords(self):
        return self.__keywords


# Create an object of keywords
key = Keyword("flexible, creative, great communication, organized, quick learner")


def find_keyword(test_string, text_to_test):
    words = re.split(r'[.,]', text_to_test)
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    word_prob_dict = {}
    size_corpus = len(words)
    for word in word_freq:
        word_prob_dict[word] = float(word_freq[word]) / size_corpus

    prob_list = []
    for word, prob in word_prob_dict.items():
        prob_list.append(prob)
    non_exist_prob = min(prob_list) / 2

    words = test_string.split()
    test_word_freq = {}
    for word in words:
        if word in test_word_freq:
            test_word_freq[word] += 1
        else:
            test_word_freq[word] = 1

    test_words_ba = {}
    for word, freq in test_word_freq.items():
        if word in word_prob_dict:
            test_words_ba[word] = freq / word_prob_dict[word]
        else:
            test_words_ba[word] = freq / non_exist_prob

    test_word_ba_list = []
    for word, ba in test_words_ba.items():
        test_word_ba_list.append((word, ba))

    def sort_func(a, b):
        if a[1] > b[1]:
            return -1
        elif a[1] < b[1]:
            return 1
        return 0

    test_word_ba_list.sort(key=lambda x: x[0])
    return test_word_ba_list
