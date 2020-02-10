'''
Name of file:  scatterplot
Author: Yan Pan
Purpose: This module is to generate a scatterplot to show the relationship between power and appearence frequency.
Module imports it: main
'''

import matplotlib.pyplot as plt
import pandas as pd

#The function use merge data and load it to the dataframe and then use scatter function to draw the diagram.
def scatterplot():
    csv_file1 = "Candidates.csv"
    csv_file2 = "1st_Avengers.csv"

    csv_data1 = pd.read_csv(csv_file1, low_memory = False)
    csv_data2 = pd.read_csv(csv_file2, low_memory = False)
    csv_df = pd.concat([csv_data1,csv_data2],axis=0,sort=False)

    xValue = list(csv_df['Sum']/csv_df['Total'])
    yValue = list(csv_df['Sum'])

    plt.title(u'Scatterplot')
    plt.xlabel('x-value')
    plt.ylabel('y-label')

    plt.legend()
    plt.xlim(0,30)
    plt.ylim(0,1000)
    plt.xticks(range(0,30,3),rotation=70)
    plt.yticks(range(0,1000,100),rotation=70)
    plt.title('Scatterplot Diagram')
    plt.scatter(xValue, yValue, s=20, c="#C627FF", marker='o')
    plt.xlabel('Power')
    plt.ylabel('Appearance Frequency')
    plt.show()


