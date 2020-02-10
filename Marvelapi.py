'''
Name of file:  Marvelapi
Author: Jun Yang, Yingxin Liang, Yan Pan, Puxing Zhao, Shaoqing Zhang
Purpose: This module is to retrieve data from official API interface by using public key and private key.
Module imports it: main
'''
import urllib.request
import json
import time
import pandas as pd
from pandas import DataFrame
import hashlib

#Scrap data from url and load the data into dataframe
def Marvelapi():
    public_key = "d39dc67a9bbc2ff4c0505a7cd0e1ae87"
    private_key = "68b08096d3088751561f83cbac4ad08e843b6bab"

    limit = 100
    offset = 0
    iterations = 15  # only <1500 characters
    df = DataFrame()
    try:
        for i in range(iterations):
            ts = str(int(time.time()))
            code = ts + private_key + public_key
            hash = hashlib.md5(code.encode('utf-8')).hexdigest()
            request_url = 'http://gateway.marvel.com/v1/public/characters?ts=%s&apikey=%s&hash=%s&limit=%s&offset=%s' % (
            ts, public_key, hash, limit, offset)
            req = urllib.request.Request(request_url)
            response = urllib.request.urlopen(req)
            data = json.loads(response.read())["data"]["results"]
            df = df.append(data, ignore_index=True)
            offset = offset + limit
            print(i)

        for col in ["comics", "events", "series", "stories"]:
            df[col] = df[col].map(lambda x: x["available"])

        ordered_df = df[["name", "comics", "series", "stories", "events"]]
        #ordered_df = ordered_df.sort("comics", ascending=False)
        ordered_df.to_csv("marvel_characters.csv", encoding='utf-8', index=False)
        #Save the json data into csv file.
    except:
        print("Due to the issues of internal server error of Marvel API, please try again later.")
