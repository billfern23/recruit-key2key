import re
from flashtext import KeywordProcessor

class Keyword:

    def __init__(self, keywords):
        self.__keywords = keywords

    def set_keywords(self, keywords):
        self.__keywords = keywords

    def get_keywords(self):
        return self.__keywords

    def get_keywords_number(self):
        return len(self.__keywords)


def find_keyword(keyword_dict, text_to_test):

    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_dict(keyword_dict)
    result = keyword_processor.extract_keywords(text_to_test)

    return result
