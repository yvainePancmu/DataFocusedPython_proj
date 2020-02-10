'''
Name of file:  first_avengers
Author: Yingxin Liang
Purpose: Create line chart and bar chart to analyze the information about the first generation of Avengers
Module imports it: main
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def first_avengers():
    # Load data and obtain the columns needed
    file_addr= "1st_Avengers.csv"
    data = pd.read_csv(file_addr)
    df = pd.DataFrame(data)
    del df['Nickname']
    del df['Real Name']
    del df['Type']
    df.index = df['Hero Name']
    del df['Hero Name']
    del df['Likes']

    # Description of 1st Avengers dataset
    median = df.median()
    mean = df.mean()
    std = df.std()
    df_first_overview = pd.DataFrame(zip(mean,median,std))
    df_first_overview.index = df.columns
    df_first_overview.columns = ['mean','median','std']
    df_first_overview

    # Plot the line plot of 1st Avengers description
    plt.plot(df.columns, mean, marker='o', mec='b', mfc='w',label='mean')
    plt.plot(df.columns, median, marker='*', ms=10,label='median')
    plt.plot(df.columns, std, marker='x', ms=10,label='std')

    plt.legend()  # show the legend
    plt.title('Description of 1st Avengers')
    plt.xticks(rotation=-90)

    # Plot the bar chart of characters' appearance in Marvel Universe
    labels = df.index

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()
    comics = ax.bar(x - 2*width, df['Comics'], width, label='Comics', color='lightskyblue')
    series = ax.bar(x - width, df['Series'], width, label='Series', color='lightcoral')
    stories = ax.bar(x, df['Stories'], width, label='Stories', color='lightseagreen')
    events = ax.bar(x + width, df['Events'], width, label='Events', color='orange')


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Frequency')
    ax.set_title('Characters\'s appearance in Marvel Universe')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.xticks(rotation=-25)
    plt.ylim(0, 4500)


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width()/2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(comics)
    autolabel(series)
    autolabel(stories)
    autolabel(events)


    fig.tight_layout()

    plt.show()