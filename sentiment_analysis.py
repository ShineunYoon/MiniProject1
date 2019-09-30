from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def analyze(*args):

    client = language.LanguageServiceClient()

    with open(args[0], 'r') as tweets:
        content = tweets.read()

    document = types.Document(content=content, type=enums.Document.Type.PLAIN_TEXT)
    analysis = client.analyze_sentiment(document=document)

    # Overall Sentiment Analysis
    score = analysis.document_sentiment.score
    magnitude = analysis.document_sentiment.magnitude
    standardized_score = (score / magnitude) * 100

    return standardized_score