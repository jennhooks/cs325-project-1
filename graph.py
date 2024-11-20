#!/usr/bin/python
# Graph.py
#
# Module holding functions to graph data using matplotlib

import matplotlib.pyplot as plyplot
import numpy

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
