"""
translator.py - A module for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.

    Args:
        englishText (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.

    Args:
        frenchText (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text
