import pandas as pd
from matplotlib import pyplot as plt

passengerdata = pd.read_csv('passenger_over_time.csv', sep=',', encoding='utf-8')


x = passengerdata['PublishDate']

y = passengerdata['WordCount']

plt.plot(x,y)

plt.ylabel('WordCount')

plt.xlabel('Date')

plt.title('\'Passenger\' Over Time')

passengerplot = plt.show()

shipdata = pd.read_csv('ship_over_time.csv', sep=',', encoding='utf-8')

x1 = shipdata["PublishDate"]
y1 = shipdata["WordCount"]

plt.plot(x1,y1)

plt.xlabel('Date')
plt.ylabel('WordCount')
plt.title('\'Ship\' Over Time')

shipplot = plt.show()
