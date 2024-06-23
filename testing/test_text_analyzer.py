import unittest
import csv
from text_analyzer import Text_Analyzer
from pathlib import Path


class TestTextAnalyzer(unittest.TestCase):

    #Sets up the list
    def setUp(self):
        character_list = []
        csv_file_path = Path(__file__).parent.parent / "characters.csv"
        with open(csv_file_path, newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                character_list.extend([value for value in row if value])
        self.text_analyzer = Text_Analyzer(character_list)

    #Mock test cases manually created
    def test_is_valid_text(self):
        self.assertTrue(self.text_analyzer.is_valid_text("Luffy"))
        self.assertTrue(self.text_analyzer.is_valid_text("Wuffy"))
        self.assertFalse(self.text_analyzer.is_valid_text("Loro"))
        self.assertTrue(self.text_analyzer.is_valid_text("Wanji"))

    #Real Test Cases from actual data scraped from Reddit
    def test_is_valid_text_real(self):
        self.assertFalse(self.text_analyzer.is_valid_text("argue with oda about it\n\nhttps://preview.redd.it/uw81xij8yl7d1.jpeg?width=975&format=pjpg&auto=webp&s=4bee22377fdaa8d284045a659e4b8554f7334d35"))


if __name__ == '__main__':
    unittest.main(buffer=False)