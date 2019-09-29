import tweepy

consumer_key = 'Y0nziezvpeBLvENio4hvF5Rwx'
consumer_secret ='KdxeyJGJEh4pLq6ebPEp3yuCBf522KLqbAvPsZOHlYgrw1o0xR'
access_token = '1171884577087873024-9O04MqVWQOUGduSKjHBOf6p6vJLXdQ'
access_token_secret = 'J4uQhozPVPU5mkp1quABrQ9FbEuiSegSp6qLmilu6o5zF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweets(*args):
   file=open('./tweet.text', 'w+')
   tweets = tweepy.Cursor(api.search,q=args[0],lang='en').items(args[1])
   for tweet in tweets:
      file.write(tweet.text)
      file.write('\n')
   file.close()
