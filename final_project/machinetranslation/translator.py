import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

class Translator(object):

    def __init__(self):
        authenticator = IAMAuthenticator(f'{apikey}')
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=authenticator
        )
        self.language_translator.set_service_url(f'{url}')   



    def englishToFrench(self, englishText):
        frenchText = self.language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
        return frenchText