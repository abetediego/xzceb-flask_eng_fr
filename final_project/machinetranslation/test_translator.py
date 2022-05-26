import unittest

from translator import Translator

class TestTranslator(unittest.TestCase): 
    def test1(self): 
        translator = Translator()
        self.assertEqual(translator.englishToFrench('Thanks'), "Merci")         

unittest.main()