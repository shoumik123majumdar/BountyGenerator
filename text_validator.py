from fuzzywuzzy import fuzz


class Text_Validator:
    def __init__(self,char_list):
        self.char_list = char_list

    def fuzzy_compare_to_list(self,phrase, word_list):
        for word in word_list:
            if fuzz.partial_ratio(word, phrase) > 80:
                return True
        return False

    def is_valid_text(self,text):
        if self.fuzzy_compare_to_list(text, self.char_list):
            return True
        return False
