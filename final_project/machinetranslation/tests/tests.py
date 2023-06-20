import unittest

from translator import french_to_english, english_to_french

class TestTranslation(unittest.TestCase):
    def test_english_to_french(self):
        english_text = "Hello"
        expected_french_text = "Pepitoooo"
        result = english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

    def test_french_to_english(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        result = french_to_english(french_text)
        self.assertEqual(result, expected_english_text)

unittest.main()