from fuzzywuzzy import fuzz

"""
Purpose: Based on a list of characters and given text, extracts insights from given text based on the list of characters
"""
class Text_Analyzer:
    def __init__(self,char_list):
        self.char_list = char_list

    """
    Helper method that uses fuzzy matching algorithm to check if given phrase (phrase) is within the character list (char_list)
    Inputs: 
        - phrase: phrase that you want to compare to the character list
    Outputs: TUPLE (returnable,characters)
        - returnable: boolean value of whether or not there was a fuzzy match between given phrase and character list
        - characters: A list of the character names so that 
    """
    def fuzzy_compare_to_list(self,phrase):
        similarity_threshold = 76  # Threshold for how similar the phrase and the character need to be
        phrase_contains_character = False  # Whether your phrase contains characters or not
        characters = []  # characters that are contained
        for word in self.char_list:
            score = fuzz.partial_ratio(word, phrase)
            #print(f"Comparing '{word}' to '{phrase}', score: {score}")  # Testing Statement
            if score>= similarity_threshold:
                phrase_contains_character = True
                characters.append(word)
        return phrase_contains_character,characters

    """
    Determines if the text is "valid" based on if the text contains a character that is also in the character list
    Inputs:
        - text: text that you want to determine is valid
    Output:
        - bool: True if the text does contain a character in the character list, False otherwise. 
    """
    def is_valid_text(self,text):
        boolean, characters = self.fuzzy_compare_to_list(text)
        return boolean

    """
    Returns a list of the characters that were found in the given text
    Inputs:
        - text: text that you want the characters from
    Output:
        - characters: a list of the characters extracted from the given text
    """
    def find_characters_in_text(self,text):
        returnable, characters = self.fuzzy_compare_to_list(text)
        return characters
