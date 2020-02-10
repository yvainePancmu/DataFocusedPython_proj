'''
Name of file:  Weight
Author: Jun Yang
Purpose: This module is to calculate the weight by using the entropy method
Module imports it: main, Prediction_appearances_and_skills
'''
import pandas as pd
import numpy as np
import math
from numpy import array

#read file
file = 'Candidates.csv'
file1 = 'Candidates.csv'
file2 = '1st_Avengers.csv'

df = pd.read_csv(file)
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
#df.dropna()
#df1.dropna()

#For Popularity, Power and Apperance
#remove unrelated columns when calculating the weights
df.drop(df.columns[16:27],axis=1,inplace=True)
df.drop(df.columns[9:15],axis=1,inplace=True)
df.drop(df.columns[:8],axis=1,inplace=True)
#print(df)

#For Popularity-candidates
df1.drop(df1.columns[:22],axis=1,inplace=True)
df1.drop(df1.columns[-1],axis=1,inplace=True)
#print(df1)

#For Popularity-1st avergener
df2.drop(df2.columns[:22],axis=1,inplace=True)
df2.drop(df2.columns[-1],axis=1,inplace=True)
#print(df2)

def cal_weight(x):
    #Normalization
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))

    #calculate K
    rows = x.index.size
    cols = x.columns.size
    k = 1.0 / math.log(rows)

    x = array(x)
    #matrix operations
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf

    # Calculate Entropy
    d = 1 - E.sum(axis=0)
    # Calculate the weight
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj
        # Calculate the points

    w = pd.DataFrame(w)
    return w

#The weights for popularity, power and appearance
w = cal_weight(df)  # call cal_weight
w.index = df.columns
w.columns = ['weight']


#The weights of popularity for candidates
w1 = cal_weight(df1)  # call cal_weight
w1.index = df1.columns
w1.columns = ['weight']

#The weights of popularity for first avengers
w2 = cal_weight(df2)  # call cal_weight
w2.index = df2.columns
w2.columns = ['weight']

