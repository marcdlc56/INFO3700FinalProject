import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from htmllist import coronaList
import pandas as pd
import articleDateExtractor
from datetime import datetime, timedelta, date
listoftext = []

start_date = '2020/02/01'
articletime = pd.to_datetime(start_date)

columnnames = ['ArticleText', 'PublishDate']
df = pd.DataFrame(columns=columnnames)

for article in coronaList:
    page = requests.get(article).text
    soup = BeautifulSoup(page, 'html5lib')

    p_tags = soup.find_all('p')
    # Get the text from each of the “p” tags and strip surrounding whitespace.
    p_tags_text = [tag.get_text().strip() for tag in p_tags]
    sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
    # Combine list items into string.
    article = ' '.join(sentence_list)

    summary = summarize(article, ratio=.9)

    summary = str(summary)
    newdata = [summary,articletime]

    df2 = pd.DataFrame({"ArticleText":[summary],
                    "PublishDate":[articletime]})
    df = df.append(df2, ignore_index=True)

    articletime = articletime + pd.DateOffset(days=1)


#df.to_csv('SummaryandPublishDate.csv', sep='\t', encoding='utf-8')

print('Done')
