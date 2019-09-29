import tweepy
import re

#

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweets(*args):
   file=open('./tweet.text', 'w+')
   tweets = tweepy.Cursor(api.search,q=args[0],lang='en').items(args[1])
   for tweet in tweets:
      text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet.text)
      file.write(text)
      file.write('\n')
   file.close()

# if __name__ == "__main__":
#     get_tweets("nike",10)
