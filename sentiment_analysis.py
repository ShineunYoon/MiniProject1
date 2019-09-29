import argparse
import sys

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def analyze(tweet_result):
    accumulative = 0

    client = language.LanguageServiceClient()

    with open(tweet_result, 'r') as tweets:
        content = tweets.read()

    document = types.Document(content=content, type=enums.Document.Type.PLAIN_TEXT)

    analysis = client.analyze_sentiment(document=document)
    score = analysis.document_sentiment.score
    magnitude = analysis.document_sentiment.magnitude

    for index, line in enumerate(analysis.sentences):
        line_score = line.sentiment.score
        accumulative =accumulative + line_score

    reliability = (accumulative / magnitude) * 100

    print('Overall Sentiment: score of {} with magnitude of {}'.format(accumulative, magnitude))
    how_reliable = reliability_checker(reliability);
    return how_reliable


def reliability_checker(reliability):
    if reliability < 20:
        return "Unreliable"
    elif 20 <= reliability < 50:
        return "Low Reliability"
    elif 50 <= reliability < 80:
        return "Possibly True"
    else:
        return "Truly Believable"


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
#     parser.add_argument('tweet_result')
#     args = parser.parse_args()
#
#     print(analyze(args.tweet_result))
