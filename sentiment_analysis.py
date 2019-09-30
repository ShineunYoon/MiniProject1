from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def analyze(*args):
    accumulative = 0

    client = language.LanguageServiceClient()

    with open(args[0], 'r') as tweets:
        content = tweets.read()

    document = types.Document(content=content, type=enums.Document.Type.PLAIN_TEXT)

    analysis = client.analyze_sentiment(document=document)
    score = analysis.document_sentiment.score
    magnitude = analysis.document_sentiment.magnitude

    for index, line in enumerate(analysis.sentences):
        line_score = line.sentiment.score
        accumulative = accumulative + line_score

    emotion = (accumulative / magnitude) * 100

    print('Overall Sentiment: score of {} with magnitude of {}'.format(accumulative, magnitude))
    comment = scorer(emotion);
    return comment


def scorer(emotion):
    if emotion < 20:
        return "Terrible"
    elif 20 <= emotion < 50:
        return "Think once again"
    elif 50 <= emotion < 80:
        return "Sounds good"
    else:
        return "Go for it!"