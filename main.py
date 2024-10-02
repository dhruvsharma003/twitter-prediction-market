import tweepy
import pandas as pd

# Authenticate with Twitter API
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweets(keyword, count=100):
    tweets = api.search(q=keyword, count=count, lang='en')
    data = [[tweet.created_at, tweet.text, tweet.user.screen_name] for tweet in tweets]
    df = pd.DataFrame(data, columns=['Timestamp', 'Tweet', 'User'])
    return df

# Example: Fetch tweets related to an event
event_tweets = get_tweets('2024 US Elections', 100)
print(event_tweets.head())