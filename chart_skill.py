"""
Name of file:  chart_skill
Author: Puxing Zhao
Purpose: Display the information about the number of heroes in each range of the skills
Module imports it: main
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#create a function chart_skills which will be used in the main method
def chart_skill():
    #read the file 'Candidates'
    table = pd.read_csv("Candidates.csv")

    #divide skills(0-7) into 4 ranges: 0-1, 2-3, 4-5, 6-7
    #calculate the number of heroes in each range of Intelligence
    i1=0#count the number of heroes in range 0-1
    i2=0#count the number of heroes in range 2-3
    i3=0#count the number of heroes in range 4-5
    i4=0#count the number of heroes in range 6-7
    for x in table['Intelligence']:
        if x==0 or x==1:
            i1 +=1
        elif x==2 or x==3:
            i2 += 1
        elif x==4 or x==5:
            i3 +=1
        else:
            i4 += 1
    #save the counters to a list
    inte = [i1, i2, i3, i4]

    #calculate the number of heroes in each range of Strength
    #similar to Intelligence
    s1=0
    s2=0
    s3=0
    s4=0
    for x in table['Strength']:
        if x==0 or x==1:
            s1 +=1
        elif x==2 or x==3:
            s2 += 1
        elif x==4 or x==5:
            s3 +=1
        else:
            s4 += 1
    stre = [s1, s2, s3, s4]

    #calculate the number of heroes in each range of speed
    sp1=0
    sp2=0
    sp3=0
    sp4=0
    for x in table['Speed']:
        if x==0 or x==1:
            sp1 +=1
        elif x==2 or x==3:
            sp2 += 1
        elif x==4 or x==5:
            sp3 +=1
        else:
            sp4 += 1
    spe = [sp1, sp2, sp3, sp4]

    #calculate the number of heroes in each range of Endurance
    e1=0
    e2=0
    e3=0
    e4=0
    for x in table['Endurance']:
        if x==0 or x==1:
            e1 +=1
        elif x==2 or x==3:
            e2 += 1
        elif x==4 or x==5:
            e3 +=1
        else:
            e4 += 1
    eud = [e1, e2, e3, e4]

    #calculate the number of heroes in each range of Energy Emission
    en1=0
    en2=0
    en3=0
    en4=0
    for x in table['Energy Emission']:
        if x==0 or x==1:
            en1 +=1
        elif x==2 or x==3:
            en2 += 1
        elif x==4 or x==5:
            en3 +=1
        else:
            en4 += 1
    eng = [en1, en2, en3, en4]

    #calculate the number of heroes in each range of Combat Skills
    c1=0
    c2=0
    c3=0
    c4=0
    for x in table['Combat Skills']:
        if x==0 or x==1:
            c1 +=1
        elif x==2 or x==3:
            c2 += 1
        elif x==4 or x==5:
            c3 +=1
        else:
            c4 += 1
    com = [c1, c2, c3, c4]

    #create a dictionary, key is the name of the skill and value is the list of number of heros in different skill sets
    category_names = ['0-1', '2-3', '4-5', '6-7']
    results = {
        'Intelligence': inte,
        'Strength': stre,
        'Speed': spe,
        'Endurance': eud,
        'Energy Emission': eng,
        'Combat Skills': com
    }


    def match(results, category_names):
        """
        Parameters
        ----------
        results : dict
            A mapping from skill labels to a list of ranges per category.
            It is assumed all lists contain the same number of entries and that
            it matches the length of *category_names*.
        category_names : list of str
            The category labels.
        """
        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.get_cmap('cool')(
            np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(11, 6))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())
        ax.set_xlabel('Number of heros in each range')
        ax.set_ylabel('Skill Name')

        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)
            xcenters = starts + widths / 2


            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, widths)):
                ax.text(x, y, str(int(c)), ha='center', va='center',
                        color=text_color)
        ax.legend(ncol=len(category_names), bbox_to_anchor=(-0.01, 1),handlelength=6.5,
                  loc='lower left', fontsize='x-large')

        return fig, ax

    #call the match function
    match(results, category_names)
    #display the chart
    plt.show()

