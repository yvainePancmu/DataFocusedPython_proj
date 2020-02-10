"""
Name of file:  Prediction_appearances_and_skills
Author: Puxing Zhao
Purpose: Display the information about the predictions of heroes based on the entrophy of appearances and skills
Module imports it: main
Module it imports: Weight
"""

import pandas as pd
import Weight

#create a function Prediction_appearances_and_skills which will be used in the main method
def Prediction_appearances_and_skills():

    W_sum = 0
    W_total = 0
    W_Pop = 0
    n = 0

    #This function allows users to choose the prediction mode
    def weight_choose(command):
        if command == 1:
            sum = Weight.w.iloc[0].item()
            total = Weight.w.iloc[1].item()
            Pop = Weight.w.iloc[2].item()
            n = 6   #number for the next avengers
        elif command == 2:
            print("Enter importance degree for 3 factors: official importance, power and popularity.")
            print("The sum of these 3 factors should equal to 1.")
            sum = float(input("Input the weights for official importance:"))
            total = float(input("Input the weights for power:"))
            Pop = float(input("Input the weights for popularity:"))
            n = int(input("Input the amount of team members(from 1 to 10):"))

        return sum,total,Pop,n

    W_sum,W_total,W_Pop,n = weight_choose(int(input("Which method do you want to use? 1:Statistic Method 2:Customized Method")))

    table = pd.read_csv('Candidates.csv')
    table1 = pd.read_csv('1st_Avengers.csv')

    # intersection of the heroes based on different skill sets
    set1 = set()
    set2 = set()
    set3 = set()
    set4 = set()
    set5 = set()
    set6 = set()

    # find the heroes who haves the skills lager than the min. of the first generation of Avenger
    for i in range(len(table.index)):
        if table['Intelligence'][i] > table1['Intelligence'].min():
            set1.add(table['Hero Name'][i])
        if table['Strength'][i] > table1['Strength'].min():
            set2.add(table['Hero Name'][i])
        if table['Speed'][i] > table1['Speed'].min():
            set3.add(table['Hero Name'][i])
        if table['Endurance'][i] > table1['Endurance'].min():
            set4.add(table['Hero Name'][i])
        if table['Energy Emission'][i] > table1['Energy Emission'].min():
            set5.add(table['Hero Name'][i])
        if table['Combat Skills'][i] > table1['Combat Skills'].min():
            set6.add(table['Hero Name'][i])
    #find the intersection of the 6 skill sets
    heroes1 = (((set1.intersection(set2).intersection(set3)).intersection(set4)).intersection(set5)).intersection(set6)
    

    # intersection of the heroes based on appearances in different medias
    set7 = set()
    set8 = set()
    set9 = set()
    set10 = set()

    # find the heroes who haves the appearances lager than the min. of the first generation of Avenger
    for i in range(len(table.index)):
        if table['Comics'][i] > table1['Comics'].min():
            set7.add(table['Hero Name'][i])
        if table['Series'][i] > table1['Series'].min():
            set8.add(table['Hero Name'][i])
        if table['Stories'][i] > table1['Stories'].min():
            set9.add(table['Hero Name'][i])
        if table['Events'][i] > table1['Events'].min():
            set10.add(table['Hero Name'][i])
    #find the intersection of the 4 sets of the appearances 
    heroes2 = (set7.intersection(set8).intersection(set9)).intersection(set10)
    
    #get the intersection fo the two sets: skills and appearances
    ins = heroes1.intersection(heroes2)

    ins = list(ins)
    #create a list score to store the sum of appearances, skills, and popularity scores
    score = []
    for ele in ins:
        for i in range(len(table.index)):
            if (table['Hero Name'][i] == ele):
                score.append((table['Sum'][i] * W_sum + table['Total'][i] * W_total + table['Pop'][i] * W_Pop))
    
    #create a dictionatory of hero names and total scores and then sort it based on total scores
    dic = dict(zip(ins, score))
    sort_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    
    #display the recommended characters
    cnt = 0;
    print("The recommended heros of next avengers are: ")
    for key, value in sort_dic.items():
        cnt += 1
        if cnt > n:
            break
        print("%s: %s" % (key, value))

