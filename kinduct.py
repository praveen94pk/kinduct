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

#Implementation
#1. Firstly, we are dropping the unwanted columns which are not useful for our current and future analysis. 
#2. The playersID got grouped by and summed up the numerical columns accordingly to support our upcoming analysis and finally stored in the summation pandas data frame.
#3. This greatly helps to answer our task 3, 4, 5, 6 and 7. 


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

#Task 3: Wins_agg: total wins / total players
        
#Calculating the winning aggregation of the players. 

#Assumptions : Assuming the winning aggregation has to be calculated according to the players level. 
#To acheive this we are grouping the data according to the players played in the hockey matches respectively. 

def task3_wins_agg(summation, total_players):
    print('Started Task 3')
    Wins_agg = (summation["W"]/total_players)
    print('Executed Task 3')
    return round(Wins_agg, 2)
    
#Implementation: 

#1. To know the total number of players played we have applied unique function to avoid duplication and stored up in the list to count the number on players played in the hockey league. 
#2. Finally, to compute the aggregations we have calculated the total number of wins by a player and divided by the total number of players as mentioned. 

#Task 4: Losses_agg: total losses / total players
        
#Calculating the Losing Average of the Players. 

#Assumptions : Assuming the lossing aggregation has to be calculated according to the players level. 
#To acheive this we are grouping the data according to the players played in the hockey matches respectively.


def task4_losses_agg(summation, total_players):
    print('Started Task 4')
    Losses= summation["L"]
    Losses_agg = round((Losses/total_players),2)
    print('Executed Task 4')
    return round(Losses_agg, 2)
    

#Implementation:

#1. The summation data frame having all the summed up numerical columns grouped by the playerID. The column L in the data frame has the losses calculated according to the players 
#2. Computation done by dividing the total losses by total number of players played.

#Task 5: GP_agg: total games played / total players
        
#Assumptions : Assuming the games played aggregation has to be calculated according to the players level. 
#To acheive this we are grouping the data accordingly to the players played in the hockey matches respectively.

def task5_gp_agg(summation, total_players):
    print('Started Task 5')
    games_played = summation["GP"]
    games_played_agg = (games_played/total_players)
    print('Executed Task 5')
    return round(games_played_agg, 2)
    


#Implementation: 

#1. The summation data frame having all the summed up numerical columns grouped according to the playerID. The column GP in
#the data frame having the summation of games played.
#2. Games played divided by the total number of players gives us the aggregation of games played.

#Task 6: Mins_over_GA_agg: Total minutes played / total goals against
        
#Assumptions : Assuming the the minutes over goals against has to be calculated according to the players level.

def task6_ga_agg(summation):
    print('Started Task 6')
    mins_over_ga = summation["Min"]/summation["GA"]
    print('Executed Task 6')
    return round(mins_over_ga, 2)
    
#Implementation: 

#1. The summation data frame having all the summed up numerical columns grouped according to the playerID. 
#2. The minutes over the goals against, column Min (Minutes) in
#the data frame having the summation of total minutes played and column GA has total goals against.

#Task 7: GA_over_SA_agg: total goals against / total shots against
        
#Assumptions : Assuming the GA over SA aggregation has to be calculated according to the players level.

def task7_ga_over_sa_agg(summation):
    print('Started Task 7')
    ga_over_sa_agg = summation["GA"]/summation["SA"]
    print('Executed Task 7')
    return round(ga_over_sa_agg, 2)
    
#Implementation: 

#1. The summation data frame has all the summed up numerical columns grouped according to the playerID. 
#2. Aggregation done by dividing summation of goals against divided by the summation of shots against.


#Task 8: avg_percentage_wins: calculate the percentage of games won for each player, then take the
#mean at team level
        
#Assumptions 1 : Assuming the average of percentage wins has to be calculated according to the players level. Grouping the data according to the players
#the players level and calculating the percentage of games won for each year.

#Assumptions 2: Assuming the mean has to be calculated according to the team level.

def task8_avg_percentage_wins(summation,summation_team,total_teams):
    print('Started Task 8')
    wins = summation["W"]
    gp = summation["GP"]
    percentage = (wins/gp) * 100 
    

#Average wins percentage according to the team level
    
    wins_team = summation_team["W"]
    mean = (wins_team/ total_teams) 
    print('Executed Task 8')
    return round(percentage, 2), round(mean, 2)
    
    
#Implementation: 
    
#1. The summation data frame having all the summed up numerical columns grouped according to the playerID. 
#2. The columns needed for our task includes summation of wins and games played to calculate the percentage. 
#3. We achieved calculating the percentage by using the formula (wins/gp) * 100 and added as a column in 
#our data frame.
#4. The summation_team data frame having all the summed up numerical columns grouped according to the teams.
#5. Finally, we achieved calculating the mean by using the formula (wins_team/ total_teams) and added as a column in 
#our data frame.

#Task 9: most_goals_stopped: {‘playerID’: playerID, ‘goals_stopped’: goals_stopped}
        
#Assumptions : Assuming the most goals stopped has to be calculated according to the players level.
#Calculating the most number of goals stopped by the goal keepers and inserting into the dictionary data type respectively. 

def task9_most_goals_stopped(summation,data):
    print('Started Task 9')
    goals_stopped= summation["SA"]
    goals_stopped
    max_goals= data.groupby(['playerID']).max()  

    res_dict = {}
    for playerID in max_goals:
        res_dict[playerID] = max_goals['SA']
    print('Executed Task 9')
    return res_dict
    
#Implementation: 

#1. Firstly, we have summed up the goals stopped by the goalies and we need to calculate the maximum number of goals stopped by the individual player respectively. 
#2. We are accessing the each row in the data frame and making it in to a dictionary. 

#Task 10: most_efficient_player: {‘playerID’: playerID, ‘efficiency’: goals_stopped / minutes played}
        
#Assumptions : Assuming the efficient player has to be calculated according to the players level
#Calculating the most efficient player with the help of goals stopped divided by the minutes played and finally inserting into the dictionary data type respectively.

def task10_most_efficient_player(summation):
    print('Started Task 10')
    res_dict2 = {}
    for playerID in summation:
        res_dict2[playerID] = summation['SA'] / summation['Min']
    print('Executed Task 10')
    return res_dict2
    

#Implementation: 

#1. Firstly, we have summed up the goals stopped and the minutes played by the goalies and then we need to aggregate by dividing those. 
#2. We are accessing the each row in the dataframe and making it in to 
#a dictionary.


