# Remember to run pip install GetOldTweets3 in terminal
import GetOldTweets3 as got
import csv
import numpy as np
import datetime as dt
import pandas as pd

# Needed variable used like this: setMaxTweets(maxTweets)
# I assume it will attempt to run forever without this criterion
maxTweets = 1000

# Need username or search variable at least
# Possible variable used like this: setUsername(username)
# username = 'realDonaldTrump'

# Possible variable used like this: setQuerySearch(search)
search = 'coronavirus'

untilDate = dt.date.today() + dt.timedelta(1)
untilDate = untilDate.strftime("%Y-%m-%d")

tweetTextList = []
tweetDateList = []

numDays = 80
i = 1
untilDate = dt.date.today() + dt.timedelta(i)
while i <= numDays:
    untilDate = untilDate.strftime("%Y-%m-%d")

    tweetCriteria = got.manager.TweetCriteria().setTopTweets(True) \
        .setQuerySearch(search).setMaxTweets(maxTweets) \
        .setSince("2020-02-01").setUntil(untilDate)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria);

    untilDate = dt.date.today() - dt.timedelta(i)
    i += 1
    for tweet in tweets:
        tweetTextList.append(tweet.text)
        tweetDateList.append(tweet.date)

dfTweets = pd.DataFrame(list(zip(tweetDateList, tweetTextList)))


# Using pandas library, it's better
dfTweets.to_csv('finalTweets.csv', sep=',', encoding='utf-8')
