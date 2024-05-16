import aspect_based_sentiment_analysis as absa
import pandas as pd
from text_validator import Text_Validator


class Sentiment_Calculator:
    def __init__(self,data,char_list):
        self.data = data
        self.sentiment_dict = dict.fromkeys(char_list)
        self.nlp = absa.load()

    def calculate_sentiment_score(self,text):


    def generate_sentiment_dict:






