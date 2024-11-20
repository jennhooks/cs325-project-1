#!/usr/bin/python
# Graph.py
#
# Module holding functions to graph data using matplotlib

import matplotlib.pyplot as plyplot
import numpy
from server import count_sentiments_list

def grouped_bar_chart(title, labels, data_dict):
    x = numpy.arange(len(labels))
    width = 0.25
    multiplier = 0
    fig, ax = plyplot.subplots(layout='constrained')
    for category, count in data_dict.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, count, width, label=category)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('Count')
    ax.set_title(title)
    ax.set_xticks(x + width, labels)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 50)

    plyplot.show()

def organize_sentiment_data(sentiments_dict, versions):
    new_dict = {
        'Negative' : [],
        'Positive' : [],
        'Neutral' : [],
        }
    for version in versions:
        sentiments = sentiments_dict[version]
        sentiment_count_dict = count_sentiments_list(sentiments)
        new_dict['Negative'].append(sentiment_count_dict['Negative'])
        new_dict['Positive'].append(sentiment_count_dict['Positive'])
        new_dict['Neutral'].append(sentiment_count_dict['Neutral'])
    return new_dict


