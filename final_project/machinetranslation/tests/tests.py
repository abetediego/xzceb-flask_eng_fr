import unittest

from .. import translator
from translator import Translator

class TestTranslator(unittest.TestCase): 

    def test_englishToFrench1(self): 
        translator = Translator()
        self.assertEqual(translator.english_to_french(''), '') 

    def test_englishToFrench2(self): 
        translator = Translator()
        self.assertEqual(translator.english_to_french('Hi'), 'Salut') 

    def test_englishToFrench3(self): 
        translator = Translator()
        self.assertEqual(translator.english_to_french('Thanks'), 'Merci')  

    def test_englishToFrench4(self): 
        translator = Translator()
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')      

    def test_frenchToEnglish1(self): 
        translator = Translator()
        self.assertEqual(translator.french_to_english(''), '') 

    def test_frenchToEnglish2(self): 
        translator = Translator()
        self.assertEqual(translator.french_to_english('Salut'), "Hi") 
    
    def test_frenchToEnglish3(self): 
        translator = Translator()
        self.assertEqual(translator.french_to_english('Merci'), 'Thank you') 
    
    def test_frenchToEnglish4(self): 
        translator = Translator()
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello') 

unittest.main()