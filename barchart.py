'''
Name of file:  barchart
Author: Yan Pan
Purpose: This module is to draw a barchart to show the proportion of appearance frequency of each characters.
Module imports it: main
'''
import matplotlib.pyplot as plt
import pandas as pd
def barchart():
    plt.rcParams['font.sans-serif']=['SimHei']

    csv_file1 = "Candidates.csv"
    csv_file2 = "1st_Avengers.csv"
    csv_data1 = pd.read_csv(csv_file1, low_memory = False)
    csv_data2 = pd.read_csv(csv_file2, low_memory = False)
    csv_df = pd.concat([csv_data1,csv_data2], sort=False)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = csv_df['Hero Name']
    value = csv_df['Comics']


    fig1, ax1 = plt.subplots()
    ax1.pie(value, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    plt.title("character appearance")
    plt.show()

