from text_analyzer import Text_Analyzer


class Sentiment_Calculator:
    def __init__(self,data,char_list):
        self.data = data
        self.sentiment_dict = dict.fromkeys(char_list)
        self.text_analyzer = Text_Analyzer(char_list)


    def calculate_sentiment_score(self,text):
        characters = self.text_analyzer.find_characters_in_text(text)

    #def generate_sentiment_dict:






