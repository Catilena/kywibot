import random
import json
import tweepy
import time
from os import environ

consumer_key = environ['API_KEY']
consumer_secret_key = environ['API_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']


def get_quotes():
    with open('data.json') as f:
        quotes_json = json.load(f)
    return quotes_json['quotes']


def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote


def create_tweet():
    quote = get_random_quote()
    tweet = """
            {}
            """.format(quote['quote'])
    reply = """
            {}
            """.format(quote['episode'])
    return tweet, reply


def tweet_quote():
    interval = 60*60*24

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    while True:
        print('getting a random quote...')
        tweet, reply = create_tweet()
        qtweet = api.update_status(tweet)
        api.update_status(status=reply, in_reply_to_status_is=qtweet.id, auto_populate_reply_metadata=True)
        time.sleep(interval)


if __name__ == "__main__":
    tweet_quote()
