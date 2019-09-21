import tweepy
consumer_key = ''
consumer_secret =''
access_token = ''
access_token_secret = ''



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

Shoemodel = input("Enter Shoe Model you would like to perform Sentiment Analysis on: ")
no_of_tweets = int(input("Enter Number of Tweets: "))
twitter_handles = []

file=open('/media/sf_Tolu_Olutayo/twitter_handles.txt', 'w+')

tweets = tweepy.Cursor(api.search,q=Shoemodel,lang='en').items(no_of_tweets)


for tweet in tweets:
   file.write(tweet.text)
   file.write('\n')


file.close()

  

