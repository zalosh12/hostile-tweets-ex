import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import re
import string
import os


class Processor :
    def __init__(self) :
        nltk.download('vader_lexicon')
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        weapons_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../data/weapon_list.txt")
        )


        with open(weapons_file_path, 'r') as f :
            self.weapons_list = set(line.lower().strip() for line in f)


    def _get_sentiment(self, text: str) -> str :
        score = self.sentiment_analyzer.polarity_scores(text)['compound']
        if score >= 0.5 :
            return "positive"
        elif score <= -0.5 :
            return "negative"
        else :
            return "neutral"

    def _get_rarest_word(self, text: str) -> str :
        text = text.lower()
        clean_text = text.translate(str.maketrans('', '', string.punctuation))
        words = clean_text.split()
        if not words :
            return ""
        word_counts = Counter(words)
        return min(word_counts, key=word_counts.get)

    def _find_weapon(self, text: str) -> str :
        for weapon in self.weapons_list :
            if weapon in text:
                return weapon
        return ""

    def process_data(self, df: pd.DataFrame) -> pd.DataFrame :
        df['sentiment'] = df['Text'].apply(self._get_sentiment)
        df['rarest_word'] = df['Text'].apply(self._get_rarest_word)
        df['weapons_detected'] = df['Text'].apply(self._find_weapon)
        df = df.rename(columns={"_id" : "id","Text":"original_text"})

        return df




