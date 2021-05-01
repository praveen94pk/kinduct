#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:01:42 2021

@author: praveen
"""

import os
os.chdir('/Users/praveen/kinduct_final_code')
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

from kinduct import *
    
def main():
    
    
    
    print(task1_string_conversion(kinduct_data))
    
    print(task2_rename(kinduct_data))

    print(task4_losses_agg(summation, total_players))

    print(task5_gp_agg(summation, total_players))

    print(task6_ga_agg(summation))

    print(task7_ga_over_sa_agg(summation))

    print(task8_avg_percentage_wins(summation,summation_team,total_teams))

    print(task9_most_goals_stopped(summation,data))

    print(task10_most_efficient_player(summation))

if __name__ == "__main__":
    main()






