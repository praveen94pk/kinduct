#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:11:19 2021

@author: praveen
"""

import os
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

#Importing the neccessary libraries for our Kinduct assessment 

import numpy as np 
import pandas as pd


kinduct_data= pd.read_csv('/Users/praveen/kinduct/Book4.csv')

data= kinduct_data.drop(columns=["stint","PostGP","PostMin","PostW","PostL","PostT","PostENG","PostSHO","PostGA","PostSA"], axis = 1)
summation = data.groupby(['playerID']).sum()

player = data["playerID"]
total_players = len(player.unique().tolist())

teams = data["tmID"]
total_teams = len(teams.unique().tolist())

summation_team = kinduct_data.groupby(['tmID']).sum()


#Downloaded the data set from Kaggle and stored as CSV file format in the local system 
#and Reading the CSV file as Data Frame using pandas library. 

#Task 1: Displaying the Column tmID (Team ID) as strings 

#Implementation : Originally the tmID is in Pandas series and now it got converted in to string. The to_string function is used to 
#convert into strings accordingly. 

def task1_string_conversion(kinduct_data):
    print('Started Task 1')
    teamid= kinduct_data["tmID"].to_string
    return(teamid)
    print('Executed Task 1')
    
#Task 2: year to Year

def task2_rename(kinduct_data):
    print('Started Task 2')
    year_change= kinduct_data.rename(columns={"year": "Year"})
    return(year_change)
    print('Executed Task 2')
    

#Implementation: The first letter of the year is in small letter and changed into capital letter by using rename function.



