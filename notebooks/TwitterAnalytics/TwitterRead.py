# Databricks notebook source
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# COMMAND ----------

#consumer key, consumer secret, access token, access secret.
ckey="kkEEOswvcFuzKxYDShbipdwDe"
csecret="6WaPsfWdNrvnuXhY8DZpIZ3OGhhfawywAuqqHtuuMbdVsavrl6"
atoken="1286975978279849984-ZZ7GDQ427dUvpdNx8qpIJohE5OUAyC"
asecret="nebnMBMhFb09OzIXU7cx9Ah1DYWVKtuREPwu5Xh0a2sR3"

# COMMAND ----------

class Listener(StreamListener):
  
      def __init__(self):
        print("Read twitter")
        
        
      def on_data(self, data):
        all_data = json.loads(data)
        
        text = all_data["text"]
        
        print(text)
          
      def on_error(self, status):
        print (status)

# COMMAND ----------

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream=Stream(auth, Listener())
twitterStream.filter(track=["covid"])
