import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import dateutil

data = pd.read_csv('words_with_wordcount_and_publishdate.csv', sep='\t', encoding='utf-8')


X = data["WordCount"]
Y = data["PublishDate"]

graph = plt.plot(X,Y)

