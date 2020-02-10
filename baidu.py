'''
Name of file:  baidu
Author: Puxing Zhao, Shaoqing Zhang
Purpose: Extract skills data from BaiduBaike(Chinese version of Wikipedia) and save it in csv file
Module imports it: main
'''
from bs4 import BeautifulSoup
import urllib.request
import pandas
import re

#define a function baidu 
def baidu():
    
    #extract data using BeautifulSoup 
    url = "https://baike.baidu.com/item/%E6%BC%AB%E5%A8%81%E4%BA%BA%E7%89%A9%E8%83%BD%E5%8A%9B%E6%95%B0%E5%80%BC/17935032?fr=aladdin#2"
    response = urllib.request.urlopen(url)  # Access and open url
    html = response.read()  # Create html object and read the source code of page
    soup = BeautifulSoup(html, 'html.parser')

    left=[]
    right=[]
    name=[]
    inte=[]
    strength=[]
    speed=[]
    endurance=[]
    energy=[]
    combat=[]


    #print(html)
    tables = soup.findAll('table')
    tables=tables[1:]
    for tab in tables:
        for tr in tab.findAll('tr'):
            left.append(str(tr.findAll('td')[1])[29])
    
    #store the score of each character in the list
    for i in range(0,len(left),3):
        inte.append(int(left[i]))

    for i in range(1,len(left),3):
        speed.append(int(left[i]))

    for i in range(2,len(left),3):
        energy.append(int(left[i]))

    for tab in tables:
        for tr in tab.findAll('tr'):
            right.append(str(tr.findAll('td')[3])[29])
    right[3]='4'

    for i in range(0,len(right),3):
        strength.append(int(right[i]))


    for i in range(1,len(right),3):
        endurance.append(int(right[i]))

    for i in range(2,len(right),3):
        combat.append(int(right[i]))

    #store the name of each character in a list
    for i in soup.findAll('div',{'class':'para'}):
        for j in i.findAll('b'):
            name.append(str(j))

    for i in range(len(name)):
        name[i]=name[i][3:len(name[i])-4]

    #remove wrong data
    for i in range(len(name)-1, -1, -1):
        if name[i] == '注：以下数值均为官方数值' or name[i] =='<br/>\u3000\u3000' or name[i] == '\u3000':
           name.pop(i)

    # Extract English words in name
    for i in range(len(name)):
        name[i] = ''.join(re.findall(r'[A-Za-z]', name[i]))
        name[i] = re.sub('[A-Z]',lambda x:' '+x.group(0),name[i])
        name[i] = name[i][1:]
    name[64] = 'Thanos'
    
    #create a data frame using pandas
    df = pandas.DataFrame(data={"col1": name, "col2": inte, "col3": strength, "col4":speed, "col5": endurance, "col6": energy, "col7":combat})
    df.columns = ["Name", "Intelligence", "Strength", "Speed", "Endurance", "Energy Emission", "Combat Skills"]
    #print all the information
    print(df)
    #save the information to baidu.csv
    df.to_csv("baidu.csv", sep=',',index=False)

