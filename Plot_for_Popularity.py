'''
Name of file:  Plot_for_Popularity
Author: Jun Yang
Purpose: 
This module is to plot 3 figures for hero independent movies
Popularity of candidates, popularity of the first avengers and the comparison between metascore and score
Module imports it: main
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Weight

def Plot_for_Popularity():
    IMDB_file = 'all-peo.csv'
    first_A = '1st_Avengers.csv'
    candidates = 'Candidates.csv'

    #Weights for candidates calculated in Weight module
    W_score = Weight.w1.iloc[0].item()
    W_meta = Weight.w1.iloc[1].item()
    W_vote = Weight.w1.iloc[2].item()
    W_gross = Weight.w1.iloc[3].item()
    W_likes = Weight.w1.iloc[4].item()

    #Weights for first avangers
    W1_score = Weight.w2.iloc[0].item()
    W1_meta = Weight.w2.iloc[1].item()
    W1_vote = Weight.w2.iloc[2].item()
    W1_gross = Weight.w2.iloc[3].item()

    IMDB_data = pd.read_csv(IMDB_file)
    first_A = pd.read_csv(first_A)
    candidates = pd.read_csv(candidates)

    #Plot the popularity for Candidates
    candidates.drop(candidates.columns[2:22],axis=1,inplace=True) #delete unrelated colomus
    candidates.drop(candidates.columns[0],axis=1,inplace=True)
    candidates['Likes'] = candidates['Likes']/100 #Adjust the likes for ploting
    candidates = candidates.sort_values(by = 'Score', ascending = False)

    total = 0

    for i in range(12):
      #calculate the popularity value for candidates
      total += (candidates.iloc[i,1])* W_score
      total += (candidates.iloc[i, 2]) * W_meta
      total += (candidates.iloc[i, 3]) * W_vote
      total += (candidates.iloc[i, 4]) * W_gross
      total += (candidates.iloc[i, 5]) * W_likes
      candidates.iloc[i,6] = total
      total = 0

    candidates.drop(candidates.index[12:], inplace=True)
    candidates = candidates.sort_values(by = 'Pop', ascending = True)
    fig = plt.figure(1)
    plt.barh(candidates['Hero Name'], candidates['Pop'],label='Popularity',color='#8478C4')

    for x,y in zip(candidates['Hero Name'],candidates['Pop']):
       plt.text(y+30, x, '%.2f' % y, ha='center', va='bottom')
    plt.xlim(0,450)
    plt.xlabel("Popularity Value")
    plt.ylabel("Movie")

    #=====================================
    #Plot the popularity for 1-st Avengers
    first_A.drop(first_A.columns[2:22],axis=1,inplace=True)
    first_A.drop(first_A.columns[0],axis=1,inplace=True)

    total1 = 0
    sum1 = []
    for i in range(6):
      #print(candidates.iloc[[i],[1]] * sco)
      total1 += (first_A.iloc[i,1])* W1_score
      total1 += (first_A.iloc[i, 2]) * W1_meta
      total1 += (first_A.iloc[i, 3]) * W1_vote
      total1 += (first_A.iloc[i, 4]) * W1_gross
      sum1.append(total1)
      total1 = 0


    first_A['Pop'] = sum1
    first_A = first_A.sort_values(by = 'Pop', ascending = True)
    fig1 = plt.figure(2)
    plt.barh(first_A['Hero Name'], first_A['Pop'],label='Popularity',color='#6B9FB8')

    for x,y in zip(first_A['Hero Name'],first_A['Pop']):
        plt.text(y+30, x, '%.2f' % y, ha='center', va='bottom')
    plt.xlim(0,450)
    plt.xlabel("Popularity Value")
    plt.ylabel("Movie")

    #============================================
    #Plot the metascore and score for all movies
    IMDB_data.drop(IMDB_data.columns[2:22],axis=1,inplace=True)
    IMDB_data.drop(IMDB_data.columns[0],axis=1,inplace=True)

    IMDB_data['Metascore'] = IMDB_data['Metascore']/10
    IMDB_data = IMDB_data.sort_values(by = 'Metascore', ascending = True)
    fig2 = plt.figure(3)
    plt.barh(IMDB_data['Hero Name'],-IMDB_data['Metascore'],facecolor='#C8BCD0',label='Metascore')
    plt.barh(IMDB_data['Hero Name'],+IMDB_data['Score'],facecolor='#7588C1',label='Rating')

    for x, y in zip(IMDB_data['Score'], np.arange(19)):
        plt.text(x + 1.5, y - 0.3, '%.1f' % x, ha='center', va='bottom')

    for x, y in zip(IMDB_data['Metascore'], np.arange(19)):
        plt.text(-x - 1.5, y - 0.3, '%.1f' % x, ha='center', va='bottom')
    plt.xlim(-10,10)
    plt.legend(loc = 9)
    plt.xlim(-12,12)

    plt.show()

