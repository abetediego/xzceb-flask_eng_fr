"""Translate module."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

class Translator():
    """Class Translator"""
    def __init__(self):
        authenticator = IAMAuthenticator(f'{apikey}')
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=authenticator
        )
        self.language_translator.set_service_url(f'{url}')

    def english_to_french(self, english_text):
        """Translate from english to french."""
        if english_text == '':
            return ''
        result = self.language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text = result['translations'][0]['translation']
        return french_text

    def french_to_english(self, french_text):
        """Translate from french to english."""
        if french_text == '':
            return ''
        result = self.language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = result['translations'][0]['translation']
        return english_text
