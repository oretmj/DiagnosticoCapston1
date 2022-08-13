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

print("Eliga una opción (1, 2, 3 o 4")
print("1. Top retweeted")
print("2. Top emisores")
print("3. Top dias")
print("4. Top hashtags")

elige = input()
while not elige in ["1", "2", "3", "4"]:
    print("Opcion invalida, intente de nuevo")

if elige == "1": 
    top_retweeted()

elif elige == "2":
    top_emiters()

elif elige == "3":
    top_days()

else:
    top_hashtagas()