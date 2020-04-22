import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter

nlp = spacy.load('en')
data = pd.read_csv('finalTweets.csv', sep=',', encoding='utf-8')

data = pd.DataFrame(data)
# we messed up and have to lose 1 tweet because we processed it wrong and it took like a few hours to make this csv
data = data.rename(columns={"04/20/2020 21:04": "TweetTime", "Just across Dutch border, study following 1,000 people in Heinsberg to create plan for how to deal with virus https://www.google.nl/amp/s/amp.theguardian.com/world/2020/mar/31/virologists-to-turn-germany-worst-hit-district-into-coronavirus-laboratory #COVIDー19": "Tweet"})
#print(data.head())

finaldf = pd.DataFrame(columns=["Tweet", "TweetTime", "CleanedTweets", "CommonWords"])
sampledata = data.head()

#
# # for i in range(len(data))

#
for i in range(len(data)):
    tweetvar = data.loc[i, "Tweet"]
    tweetdatevar = data.loc[i, "TweetTime"]

    lemmatizedData = []
    pronounFilter = []
    stopwordFilter = []
    punctuationFilter = []
    dataAfterNounFilter = []

    doc = nlp(str(tweetvar))

    for token in doc:
        lemmatizedData.append(token.lemma_)

    for token in lemmatizedData:
        if token != "-PRON-":
            pronounFilter.append(token.lower().strip())

    stopwords = list(STOP_WORDS)

    for token in pronounFilter:
        if token != stopwords:
            stopwordFilter.append(token)

    #custom_remove_list = ['our', 'live', 'coverage', 'of', 'the', 'has', 'moved', 'here', '\\n']

    # dataAfterCustomStopWords = []
    # for word in stopwordFilter:
    #     if word not in custom_remove_list:
    #         dataAfterCustomStopWords.append(word)

    # dataAfterRemoveCoverage = []
    # for c in dataAfterCustomStopWords:
    #     if c != 'coverage':
    #         dataAfterRemoveCoverage.append(c)

    # I used my own punctuation list because we need exclamation points for the vader scoring
    # algorithm
    punctuations = ['@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '~', '`',
                    '=', '<', '>', '/', '?', '\\', ]

    for token in stopwordFilter:
        if token not in punctuations:
            punctuationFilter.append(token)

    for value in punctuationFilter:
        td = nlp(value)
        for t in td:
            if t.pos_ == 'NOUN':
                dataAfterNounFilter.append(t)

    dataAfterNounFilterStringFormatting = []

    for nlpObject in dataAfterNounFilter:
        nlpObjectIntoString=str(nlpObject)
        dataAfterNounFilterStringFormatting.append(nlpObjectIntoString)

    cleaned_data_list = dataAfterNounFilterStringFormatting

    word_freq = Counter(cleaned_data_list)
    commonWords = word_freq.most_common(5)
    # print(cleaned_data_list)
    df2 = pd.DataFrame({"Tweet": [tweetvar],
                        "TweetTime": [tweetdatevar],
                        "CleanedTweets": [cleaned_data_list],
                        "CommonWords": [commonWords]})

    finaldf = finaldf.append(df2, ignore_index=True)

finaldf.to_csv('cleanedTweets.csv', sep=',', encoding='utf-8')
