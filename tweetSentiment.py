import pandas as pd
import spacy
import nltk
from spacy.lang.en import English

from nltk.sentiment.vader import SentimentIntensityAnalyzer

parser = English()
nltk.download('vader_lexicon')

SA = SentimentIntensityAnalyzer()

tweetsentimentlist = []
tweetdatelist = []

finaldf = pd.DataFrame(columns=["SentimentScore", "TweetTime"])


def listToString(lst):
    return ' '.join(lst)


nlp = spacy.load('en')

data = pd.read_csv('cleanedTweets.csv', sep=',', encoding='utf-8')

# for i in range(len(data))
for i in range(len(data)):
    lemmatizedData = []
    cleantweetvar = data.loc[i, "CleanedTweets"]
    tweetdatevar = data.loc[i, "TweetTime"]
    doc = nlp(cleantweetvar)

    tweetdatevar = tweetdatevar[:10]
    if cleantweetvar != '':
        for token in doc:
            lemmatizedData.append(token.lemma_)

        removelist = ['[', ']', '\'', ',']
        cleanlist = []
        for item in lemmatizedData:
            if item not in removelist:
                cleanlist.append(item)

        cleanup = listToString(cleanlist)

        sentimentscore = str(SA.polarity_scores(cleanup)['compound'])

        tweetsentimentlist.append(sentimentscore)
        tweetdatelist.append(tweetdatevar)
        d = {'SentimentScore': tweetsentimentlist, 'TweetTime': tweetdatelist}

        tempdf = pd.DataFrame(d, columns=["SentimentScore", "TweetTime"])
        finaldf = finaldf.append(tempdf, ignore_index=True)

        tweetsentimentlist = []
        tweetdatelist = []
        cleanlist = []

finaldf.to_csv('tweetSentimentOverTime.csv', sep=',', encoding='utf-8')
