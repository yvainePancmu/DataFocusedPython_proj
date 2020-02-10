'''
Name of file:  Relationship
Author: Jun Yang, Yingxin Liang, Yan Pan, Puxing Zhao, Shaoqing Zhang
Purpose: This module is to scrape data of hero relationship via json data
Module imports it: main
'''
import json
import requests

def Relationship():
    #define the header for the user request
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    url = 'https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/data/marvel-data.json'
    response = requests.get(url=url, headers=headers) #get the response from the website
    result = json.loads(response.text)

    num = 0
    names = []
    item = {0: 'friend', 1: 'enemy', 2: 'creation', 3: 'family', 4: 'work', 5: 'love'} #create dictionary for analysis

    #Collect the data based on json data
    #Use key to locate the value
    for i in result['relationship']:
        #extract data by using the key
        subject = result['relationship'][i]['id']
        object = result['relationship'][i]['target_id']

        #create the name list of all characters
        if subject not in names:
            names.append(subject)
        if object not in names:
            names.append(object)

        #create a file to store all relationship for all characters
        relation = int(result['relationship'][i]['relationship'])
        with open('relation_message.csv', 'a+') as f:
            f.write(subject + ',' + object + ',' + item[relation] + '\n')

    #create a file to store ID and character names
    for j in names:
        num += 1
        with open('names_message.csv', 'a+') as f:
            f.write(j + ',' + str(num) + '\n')

    #create a file to store id, name,status and species for all characters
    for k in result['characters']:
        id = result['characters'][k]['id']
        name = result['characters'][k]['name']
        status = result['characters'][k]['status']
        species = result['characters'][k]['species']
        with open('message.csv', 'a+') as f:
            f.write(id + ',' + name + ',' + status + ',' + species + '\n')

    print("The data has been stored in the files.")