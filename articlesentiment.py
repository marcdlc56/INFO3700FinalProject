import pandas as pd
import spacy
import nltk
from spacy.lang.en import English

from nltk.sentiment.vader import SentimentIntensityAnalyzer

parser = English()
nltk.download('vader_lexicon')

SA = SentimentIntensityAnalyzer()

articlesentimentlist = []
articledatelist = []

finaldf = pd.DataFrame(columns=["SentimentScore", "articleTime"])


def listToString(lst):
    return ' '.join(lst)


nlp = spacy.load('en')

data = pd.read_csv('tokenized_words_with_wordcount.csv', sep='\t', encoding='utf-8')

# for i in range(len(data))
for i in range(len(data)):
    dataAfterLemmaFilter = []
    cleanarticlevar = data.loc[i, "CleanedArticleText"]
    datevar = data.loc[i, "PublishDate"]
    doc = nlp(cleanarticlevar)

    datevar = datevar[:10]
    if cleanarticlevar != '':
        for token in doc:
            dataAfterLemmaFilter.append(token.lemma_)

        removelist = ['[', ']', '\'', ',']
        cleanlist = []
        for item in dataAfterLemmaFilter:
            if item not in removelist:
                cleanlist.append(item)

        cleanup = listToString(cleanlist)

        sentimentscore = str(SA.polarity_scores(cleanup)['compound'])

        articlesentimentlist.append(sentimentscore)
        articledatelist.append(datevar)
        d = {'SentimentScore': articlesentimentlist, 'articleTime': articledatelist}

        tempdf = pd.DataFrame(d, columns=["SentimentScore", "articleTime"])
        finaldf = finaldf.append(tempdf, ignore_index=True)

        articlesentimentlist = []
        articledatelist = []
        cleanlist = []


finaldf.to_csv('articleSentimentOverTime.csv', sep=',', encoding='utf-8')