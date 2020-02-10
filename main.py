"""
Name of file:  main
Author: Jun Yang, Puxing Zhao, Shaoqing Zhang
Purpose: The entry point of the main method. Users can interact with our application through the main method.
Module it imports: all other modules
"""

#import all the functions
import baidu as bd
import barchart as bc
import chart_skill as cs
import first_avengers as fa
import IMDb
import maoyan as my
import Marvelapi as ma
import Plot_for_Popularity as pfp
import Prediction_appearances_and_skills as paas
import Relationship as rs
import scatterplot as sp
import word_cloud as wc

#define the main menu
def Menu():  
    print()
    print('WHO WILL BE THE NEXT AVENGERS?'.rjust(40,' '))
    print()
    print("Enter '1' to start Data Scraping")
    print("Enter '2' to start Multi-dimentional Character Analysis")
    print("Enter '3' to start New Avengers Prediction")
    print("Enter '0' to exit.", end="")
    print()
    
#display the main menu of our application
Menu()

#let users choose the information they need by enter different numbers
i=int(input("Please enter the number: "))
while i!=0 and i!=1 and i!=2 and i!=3:
    i=int(input("Wrong input! Please enter a number from 0 to 3: "))
while i!=0:  
    if i == 1:
        print("------------------------------------")
        print("Enter '1' to scrape Marvel API ")
        print("Enter '2' to scrape IMDB")
        print("Enter '3' to scrape Maoyan")
        print("Enter '4' to scrape Power Grip")
        print("Enter '5' to scrape Relationships")
        k=int(input("Please enter the number: "))
        if k == 1:
            ma.Marvelapi()
            print("Go back to MENU.")
            Menu()  
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
               i=int(input("Wrong input! Please enter a number from 0 to 3: "))
        elif k == 2:
            IMDb.IMDb();
            print("Go back to MENU.")
            Menu()
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
               i=int(input("Wrong input! Please enter a number from 0 to 3: "))
        elif k == 3:
            my.maoyan()
            print("Go back to MENU.")
            Menu()
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
               i=int(input("Wrong input! Please enter a number from 0 to 3: "))
        elif k == 4:
            bd.baidu()
            print("Go back to MENU.")
            Menu()
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
               i=int(input("Wrong input! Please enter a number from 0 to 3: "))
        else:
            rs.Relationship()
            print("Go back to MENU.")
            Menu()
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
               i=int(input("Wrong input! Please enter a number from 0 to 3: "))
    elif i == 2:
        print("------------------------------------")
        print("Enter '1' to start 1st Generation Avenger Analysis")
        print("Enter '2' to start Candidates Analysis")
        print("Enter '3' to start Independent Film Analysis")
        k=int(input("Please enter the number: "))
        while k!=1 and k!=2 and k!=3:
            k=int(input("Wrong input! Please enter a number from 0 to 3: "))       
        if k == 1:
            print("Display the information of Desciptive Analysis and Frequency in Comics: ")
            fa.first_avengers()
            #print(fa.first_avengers().df.describe())
            print("Go back to MENU.")
            Menu()
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
                i=int(input("Wrong input! Please enter a number from 0 to 3: "))
        elif k == 2:
            print("Display the information of Frequency in Comics, Relationship of Power and Frequency, and Power Distribution")
            bc.barchart()
            sp.scatterplot()
            cs.chart_skill()
            print("Go back to MENU.")
            Menu()
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
                i=int(input("Wrong input! Please enter a number from 0 to 3: "))
        elif k == 3:
            print("Display the information of Popularity, Meta Score VS Audience Rating, Comment Visualization")
            pfp.Plot_for_Popularity()            
            print("Wordcloud image is generating...Please wait patiently.")
            wc.word_cloud()
            print("Go back to MENU.")
            Menu()
            i=int(input("Please enter the number: "))
            while i!=0 and i!=1 and i!=2 and i!=3:
                i=int(input("Wrong input! Please enter a number from 0 to 3: "))

    elif i==3:
        paas.Prediction_appearances_and_skills()
        print("Thank you for using our service. See you next time!")
        break;
        # i=int(input("Please enter the number: "))
        # while i!=0 and i!=1 and i!=2 and i!=3:
        #     i=int(input("Wrong input! Please enter a number from 0 to 3: "))

