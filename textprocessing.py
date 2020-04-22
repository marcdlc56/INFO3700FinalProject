import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
import pandas as pd
nlp = spacy.load('en')
wordlist = []

data = pd.read_csv('SummaryandPublishDate.csv', sep='\t', encoding='utf-8')

finalcolumnnames = ['ArticleText', 'PublishDate','CleanedArticleText','CommonWords']
df = pd.DataFrame(data)
finaldf = pd.DataFrame(columns=finalcolumnnames)
mostcommonwordsdf = pd.DataFrame(columns=["Words", "Values", "PublishDate"])

finalworddf = pd.DataFrame(columns=["Words", "WordCount", "PublishDate"])


#for i in range(len(df)):
for i in range(10):
    articletextvar = df.loc[i, "ArticleText"]
    publishdatevar = df.loc[i, "PublishDate"]

    dataAfterLemmaFilter = []
    dataAfterPronounFilter = []
    dataAfterStopwords = []
    dataAfterPunctuations = []
    dataAfterNounFilter = []

    doc = nlp(str(articletextvar))

    for token in doc:
        dataAfterLemmaFilter.append(token.lemma_)

    for token in dataAfterLemmaFilter:
        if token != "-PRON-":
            dataAfterPronounFilter.append(token.lower().strip())

    stopwords = list(STOP_WORDS)

    for token in dataAfterPronounFilter:
        if token != stopwords:
            dataAfterStopwords.append(token)

    custom_remove_list = ['our', 'live', 'coverage', 'of', 'the', 'has', 'moved', 'here', '\\n']

    dataAfterCustomStopWords = []
    for word in dataAfterStopwords:
        if word not in custom_remove_list:
            dataAfterCustomStopWords.append(word)

    dataAfterRemoveCoverage = []
    for c in dataAfterCustomStopWords:
        if c != 'coverage':
            dataAfterRemoveCoverage.append(c)

    # I used my own punctuation list because we need exclamation points for the vader scoring
    # algorithm
    punctuations = ['@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '~', '`',
                    '=', '<', '>', '/', '?', '\\', ]

    for token in dataAfterRemoveCoverage:
        if token not in punctuations:
            dataAfterPunctuations.append(token)

    for value in dataAfterPunctuations:
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

    df2 = pd.DataFrame({"ArticleText": [articletextvar],
                        "PublishDate": [publishdatevar],
                        "CleanedArticleText": [cleaned_data_list],
                        "CommonWords": [commonWords]})

    finaldf = finaldf.append(df2, ignore_index=True)

    from operator import itemgetter
    worddf = pd.DataFrame(columns=["Word", "WordCount", "PublishDate"])

    worddatelist = []
    wordnamelist = []
    wordcountlist = []

    words1 = list(map(itemgetter(0), commonWords))
    wordcount2 = list(map(itemgetter(1), commonWords))

    for word in range(len(words1)):
        worddatelist.append(publishdatevar)

    for y in words1:
        wordnamelist.append(y)

    for x in wordcount2:
        wordcountlist.append(x)

    d = {'Words': wordnamelist, 'WordCount': wordcountlist, 'PublishDate': worddatelist}

    worddf = pd.DataFrame(d, columns=["Words","WordCount", "PublishDate"])

    finalworddf = finalworddf.append(worddf, ignore_index=True)


#finaldf.to_csv('tokenized_words_with_wordcount.csv', sep='\t', encoding='utf-8')

#finalworddf.to_csv('words_with_wordcount_and_publishdate.csv', sep='\t', encoding='utf-8')
