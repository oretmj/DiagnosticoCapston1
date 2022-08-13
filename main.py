import pandas as pd
from pandas.io.json import json_normalize

# Use parte del codigo entregado en la misma pagina donde se encontraba el JSON
# https://www.kaggle.com/code/prathamsharma123/clean-raw-json-tweets-data

print("hola")

# raw_tweets = pd.read_json('farmers-protest-tweets-2021-03-5.json', lines=True)
# raw_tweets = raw_tweets[raw_tweets['lang']=='en']
# print("Shape: ", raw_tweets.shape)
# print(raw_tweets.head(5))

def top_retweeted():
    raw_tweets = pd.read_json('farmers-protest-tweets-2021-03-5.json', lines=True)
    raw_tweets = raw_tweets[raw_tweets['lang']=='en']
    top = raw_tweets.sort_values("retweetCount", ascending=False)
    print(top.head(10))


def top_emiters():
    raw_tweets = pd.read_json('farmers-protest-tweets-2021-03-5.json', lines=True)
    raw_tweets = raw_tweets[raw_tweets['lang']=='en']
    emiters = raw_tweets["user"].value_counts()
    print(emiters)
    # print(raw_tweets.columns)

def top_days():
    pass

def top_hashtagas():
    pass

top_emiters()