import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('tweetAveragesPlot.csv', sep=',', encoding='utf-8')

X = data["TweetDate"]
Y = data["AverageDailySentimentScore"]

plt.plot(X,Y,)

plt.xlabel = 'TweetDates'
plt.ylabel = 'SentimentScore'
plt.show()
