# import NLU dependencies
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions

# get the credentials
from Credentials import Credentials

class WatsonNLU:
    def __init__(self):
        # initialize NLU with watson credentials
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
            version=Credentials.watson_version,
            username=Credentials.watson_username,
            password=Credentials.watson_password,
            url=Credentials.watson_url
        )

    # send text for analysis to watson
    def analyze(self,analysisText):
        response = self.natural_language_understanding.analyze(
            text=analysisText,
            # set the nlu features required in response
            features=Features(
                keywords=KeywordsOptions(
                    emotion=True,
                    sentiment=True,
                    limit=2))).get_result()
        # check the overall sentiment in the tweet
        self.checkMood(response)

    # accepts the response from watson analysis
    def checkMood(self, response):
        