'''
Name of file:  woud_cloud
Author: Shaoqing Zhang
Purpose: This module displays wordcloud image
Module imports it: main
'''
import numpy as np
import pandas as pd
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt


def word_cloud():
    # Read excel
    sheet = pd.read_excel('avenger.xlsx',header = None)
    column = sheet[3]

    '''
    # Read csv
    with open('antman.csv',encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[3] for row in reader]
    '''

    # Combine the strings in the list together
    content0 = []
    for i in column:
        content0.append(str(i))
    content = ''.join(content0)

    # Read txt
    stopwords = [line.strip() for line in open('stopwords.txt',encoding = 'UTF-8').readlines()]

    # Use jieba to cut words
    words  = jieba.lcut(content)
    counts = {}

    # Remove stopwords
    for word in words:
        if word not in stopwords:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word,0) + 1
    items = list(counts.items())

    # Use two lists to record the results
    x = []
    n = []
    for i in items:
        x.append(i[0])
        n.append(i[1])


    # Translate Chinese to English
    from translate import Translator
    translator= Translator(from_lang="chinese",to_lang="english")
    x_trans = []
    #for i in range(300):
    for i in range(10):
        trans = translator.translate(x[i])
        x_trans.append(trans)

    # Combine two lists into dataframe
    combine = {"Word": x_trans, "Number": n[0:len(x_trans)]}
    #combine = {"Word": x, "Number": n[0:len(x)]}
    df=pd.DataFrame(combine)

    # Sort the words by its appearance number
    df.sort_values("Number",inplace=True,ascending=False)

    # Print the top 50 frequent words
    df1 = df.iloc[:50]
    print(df1)

    # Use wordcloud ot draw image
    mask = np.array(Image.open('antman_back1.png'))
    wc = wordcloud.WordCloud(
        background_color = 'white',
        max_words = 10,
    #    max_words = 300,
        mask = mask)

    #y = dict(zip(x,n))
    y = dict(zip(x_trans,n))
    wc.generate_from_frequencies(y)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    
    # Save to png
    #wc.to_file('avenger_cloud300.png')