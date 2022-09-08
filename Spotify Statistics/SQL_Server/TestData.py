import pandas as pd
import matplotlib.pyplot as plt
from Tools.Tools import convertMillis

'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This file contains functions to work with a csv file recieved from ServerConnect.py to place the data from the database into graphs
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


def TopList(data, length, List, Time = 1):
    Array = data[List].tolist()
    count = {}
    for i in Array:
        count[i] = count.get(i, 0) + 1
    sorted_dict = {}
    sorted_keys = sorted(count, key=count.get)
    if Time == 1: #Having Time at 0 gets the shortest songs from the Server
        sorted_keys = reversed(sorted_keys)

    for w in sorted_keys:
        sorted_dict[w] = count[w]
    x, y = list(sorted_dict.keys()), list(sorted_dict.values())

    plt.barh(x[:length], y[:length])
    plt.show()

def TopPopularSong(data, length, Time = 1):
    Song, Pop = data['Song'].tolist(), data['Popularity'].tolist()
    dict = {}
    for i  in range(len(Song)):
        if Song[i] not in dict:
            dict[Song[i]] = Pop[i]
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get)
    if Time == 1: #Having Time at 0 gets the shortest songs from the Server
        sorted_keys = reversed(sorted_keys)
    for w in sorted_keys:
        sorted_dict[w] = dict[w]

    x, y = list(sorted_dict.keys()), list(sorted_dict.values())

    plt.barh(x[:length], y[:length])
    plt.xlim(0,100)
    plt.show()

def TopSongLength(data, length, Time = 1):
    Song, Duration = data['Song'].tolist(), data['Duration'].tolist()
    dict = {}
    for i  in range(len(Song)):
        if Song[i] not in dict:
            dict[Song[i]] = Duration[i]
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get)
    if Time == 1: #Having Time at 0 gets the shortest songs from the Server
        sorted_keys = reversed(sorted_keys)
    for w in sorted_keys:
        sorted_dict[w] = dict[w]

    x, y = list(sorted_dict.keys()), list(sorted_dict.values())
    if Time == 1:
        y = list(reversed(y[:length]))
        x = list(reversed(x[:length]))
    else: 
        y = y[:length]
        x = x[:length]

    plt.barh(x, y)
    plt.xlim([0, max(y)+ max(y)/(max(y)/10)])
    values = list(plt.xticks())[0]
    labellist = [convertMillis(x) for x in values]
    plt.xticks(rotation=45, ha="right")
    plt.xticks(values, labellist)
    
    plt.show()

def ActiveHour(data):
    Song, Hour = data['Song'].tolist(), data['Time'].tolist()
    dict = {x: 0 for x in range(24)}
    print(dict)
    for i  in range(len(Song)):
            dict[int(Hour[i][:2])] +=1

    x, y = list(dict.keys()), list(dict.values())
    print(x)
    plt.bar(x, y)
    values = [0, 3, 6, 9, 12, 15, 18, 21]
    labellist = ['12AM', '3AM', '6AM', '9AM', '12PM', '3PM', '6PM', '9PM']
    plt.xticks(values, labellist)
    plt.show()





    
csvFile = '..\Spotify Statistics\SQL_Server\Data\stats.csv'
data = pd.read_csv(csvFile)
Artists = 'Artist'
Songs = 'Song'
Albums = 'Album'

TopList(data, 10, Albums)




