import tweepy
consumer_key = '7aybdIZTDuBFiq1moEyKhRYGe'
consumer_secret ='LRDbWiaTPnfre3v4PRlrc1cSWcXuP8XTRH5yihVATkgB3CHyTE'
access_token = '1171884577087873024-JOazU8fgLKOIoq8PAwuMbVhEciRDh3'
access_token_secret = 'iStiWwZNtjvBXOJX1PXRm6vrmrIJ8aCQOQXgD3QJaWiOm'



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

  

