# INFO3700FinalProject
Collection of Code for INFO3700 Sentiment Analysis Project

### Goal of Project ###
The goal of this project was to track the sentiment of various tweets and news articles and see if there are any trends 
we can determine. To analyze sentiment we used the VADER sentiment analysis library from NLTK to process all of our tweets. 
To find common words we used the Spacy 'en_core_web_sm' model to process the documents and the collections library to find 
the top 10 common words for each article and top 5 common words for each tweet. 
#### Project Results #### 
We found various words that popped up for different periods of time and we plotted them, such as 'Ship' and 'Passenger' which 
makes sense given that the biggest news about corona was that a passenger on a ship had it from February 7th to about March 4th. 
We also found that the tweets about COVID-19 were surprisingly all negative, they never went higher than a 0.05 on the compound
VADER sentiment score. We also found that the sentiment of the nes involving coronavirus was very volatile the last few months, 
but there were some trends in the early days in February. 


###Start to end of Project###
1. To start the project run webscraper.py, this will import a list of articles from htmlist.py, 
This script will also provide a csv of the text of each article and the date associated with the article, (as a note, we weren't
able to programmatically get the publish date for each article without running into a lot of formatting issues, and about 50 if statements, 
so we manually grabbed each publish date and used that, so to re-use this code you will need to update the webscraper to get the correct publishdate. 
2. Next run textprocessing.py, this will process each of the documents using Spacy to tokenize the articles, remove stop-words, 
lemmatize each token, remove punctuation, as well as remove any other words that we wanted to remove, in this case we removed 
a few words that were common throughout each article that were only related to CNN, not COVID-19. 
  This script will also use the collections.counter library to map out the common words for each article. The data from this 
script will be put into a CSV using Pandas. 
3. Next run article sentiment, that will re-tokenize each word for each article (we did this because we input the cleaned doc 
as a list because we didn't want to restring it together in the text processing step.) This will remove the brackets and any 
unnecessary punctuation from the list, we did decide to leave '!' in the tokens, because the exclamation mark affects the 
VADER sentiment analysis pretty heavily. Next the script will reappend each token to a new string and run that string through 
the VADER sentiment analysis model, which will then append the article publishdate and the compound sentiment score to a new csv. 
4. We aggregated the words using pivottables in a CSV, so to recreate this with a new project it will take some manual work, but 
we found that using a pivottable for the csv's was the best/quickest way we knew how to get aggregate data for each word. 
5. We then created new csv's for each observation we found useful in the pivottables. 
6. We plotted each observation over time using matplotlib, we weren't able to figure out how to only show specific tick marks
on the x-axis without taking out data, so we left it in, but it left a pretty big image, so you'll need to zoom in quite a bit 
to see the dates, but the trends are clearly visible. To replot them run words_over_time_plot.py, mostPopularWords.py, and specificwordsovertime.py. 

###Tweets###

Process is the same framework as the articles above, we scraped originally 300,000 tweets using GetOldTweets3, but we truncated
that down to about 50 tweets per day which is roughly 4,000 cells. 
The script order for tweets goes. 

GetOldTweets.py

processTweets.py

tweetSentiment.py

plotTweets.py
