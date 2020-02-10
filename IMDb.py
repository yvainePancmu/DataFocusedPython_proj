'''
Name of file:  IMDb
Author: Yingxin Liang
Purpose: Extract data from IMDb and save it in a csv file
Module imports it: main
'''
from bs4 import BeautifulSoup
import urllib.request
import re

def IMDb():
    # a film list of Marvel Cinematic Universe
    url = 'https://www.imdb.com/list/ls060663456/?sort=list_order,asc&st_dt=&mode=detail&page=1&ref_=ttls_vm_dtl'
    request_data = urllib.request.urlopen(url)
    soup = BeautifulSoup(request_data,"html.parser")
    print ('Start')
    # open the file for saving data
    csv = open('result_IMDb.csv', 'wt')
    # find all the information needed, one movie is included in one div
    movie = soup.find_all('div',class_='lister-item-content')
    name = []
    rating = []
    metascore = []
    runtime = []
    genre = []
    votes = []
    gross = []
    vote_and_gross = []

    # find all the information based on the html structure
    for i in range(0,len(movie)):
        name.append(movie[i].find('a',href=re.compile('/title/')).text)
        rating.append(movie[i].find('span',class_='ipl-rating-star__rating').text)
        metascore.append(movie[i].find('span',class_=["metascore","favorable"]).text.strip())
        runtime.append((movie[i].find('span',class_='runtime')).text)
        genre.append((movie[i].find('span',class_='genre')).text.strip().replace(" ","").replace(",","|"))
        vote_and_gross = movie[i].find_all('p',class_=["text-muted","text-small"])[2].find_all('span')

        vote_start = str(vote_and_gross[1]).find("\"") + 1
        vote_end = str(vote_and_gross[1]).find("\"",vote_start)
        votes.append(str(vote_and_gross[1])[vote_start:vote_end])

        gross_start = str(vote_and_gross[4]).find("\"") + 1
        gross_end =  str(vote_and_gross[4]).find("\"",gross_start)
        gross.append(str(vote_and_gross[4])[gross_start:gross_end].replace(",",""))

    # write the header into the file
    csv.write("name," + "rating," + "metascore," + "runtime," + "genre," + "votes," + "gross" + '\n')
    # write the data into the file
    for i in range(len(name)):
         csv.write(name[i] + "," + rating[i] + "," + metascore[i] + "," + runtime[i] + "," + genre[i] + "," + votes[i] + "," + gross[i] + '\n')
         csv.flush()
         print(name[i] + "," + rating[i] + "," + metascore[i] + "," + runtime[i] + "," + genre[i] + "," + votes[i] + "," +gross[i] + '\n')

    #close the file
    csv.close()


    print ('Finish')