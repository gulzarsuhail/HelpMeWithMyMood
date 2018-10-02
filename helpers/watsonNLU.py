# import NLU dependencies
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions

# get the credentials
from credentials import Credentials

# initialize NLU with watson credentials
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version=Credentials.watson_version,
    username=Credentials.watson_username,
    password=Credentials.watson_password,
    url=Credentials.watson_url
)

# send text for analysis to watson
def analyze(analysisText):
    response = natural_language_understanding.analyze(
        text=analysisText,
        # set the nlu features required in response
        features=Features(
            keywords=KeywordsOptions(
                emotion=True,
                sentiment=True,
                limit=2))).get_result()
    # check the overall sentiment in the tweet
    return (checkMood(response))

# accepts the response from watson analysis
def checkMood(response):
    emotion = Emotion()
    # add analysis of each keword to overall analysis
    for word in response["keywords"]:
        emotion.addKeywordAnalysis(word)
    # analize the emotion
    emotion.analyzeEmotion()
    # return the emotion
    return ({
        'emotion': emotion.emotion,
        'sentiment': emotion.sentiment
    })


class Emotion:

    # initialize emotion properties
    def __init__(self):
        self.emotion = ""
        self.sentiment = 0
        self.ems = ['sadness', 'joy', 'fear', 'disgust', 'anger']
        self.ems_score = [0, 0, 0, 0, 0]

    # add the data from keyword to the analysis
    def addKeywordAnalysis(self, keyword):
        for em in range(0, 5):
            self.ems_score[em] += keyword['emotion'][self.ems[em]]
        self.sentiment += keyword['sentiment']['score']

    # derive the most prominent emotion
    def analyzeEmotion(self):
        maxEmotion = -1000.00
        for em in range(0, 5):
            if (self.ems_score[em] > maxEmotion):
                self.emotion = self.ems[em]
                maxEmotion = self.ems_score[em]