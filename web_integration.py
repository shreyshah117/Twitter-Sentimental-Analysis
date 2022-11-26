import json

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import streamlit as st

import plotting
#consumer key, consumer secret, access token, access secret.
import sentiment_mod
import updated_v2

html_temp = '<h2>Accessing the data from Twitter. <br>Please wait a moment..</h2>'
st.markdown('''<h1>Welcome to Live Twitter Sentiment Analysis</h1> <br>
                <h3>Enter the topic you are interested in :</h3>''', unsafe_allow_html=True)




ckey="HpWwGr0Vvfhr5LhsmZyvIbGTW"
csecret="rNXbH1UsZ87qJO4Uz9BsAPLriwU4iuhRo6kE2rjJdb0DVahhMU"
atoken="1381813794817462274-5opX0C9K6wCMo86HWYa2a9YGNqzudY"
asecret="QJoXDIS0LbWE9PAGnleIiCNwNB8Nb5GAyvOtXbJ4jslZ7"

open('twitter-out.txt', 'w').close()

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']
        sentiment_value, confidence = updated_v2.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open('twitter-out.txt', 'a')
            output.write(str(sentiment_value))
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


user_input = st.text_input("")

if st.button('Show Visualisation'):
    st.markdown(html_temp, unsafe_allow_html=True)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[user_input])



