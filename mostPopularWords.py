import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
data = pd.read_csv('top_20_words.csv', sep=',', encoding='utf-8')

figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')

top10 = data[:10]
next10 = data[10::]

x = top10["Words"]
y = top10["WordCount"]

plt.bar(x,y)
plt.xlabel = 'Common Words'
plt.ylabel = 'Word Count'
plot1 = plt.show()


x1 = next10["Words"]
y1 = next10["WordCount"]

plt.bar(x1,y1,)

plt.xlabel = 'Common Words'
plt.ylabel = 'Word Count'

plot2 = plt.show()
