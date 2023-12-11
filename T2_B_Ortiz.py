# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 22:25:08 2023

@author: artur
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# A - Create the dataframe
data = {
    'State': ['CA', 'TX', 'FL', 'NY', 'IL', 'PA'],
    'TimeZone': ['PST', 'CST', 'EST', 'EST', 'CST', 'EST'],
    'Population': [39250, 27862, 20612, 19745, 12801, 12784],
    'Percentage': [12, 9, 6, 6, 4, 4]
}

dataframe = pd.DataFrame(data)
print("Original Dataframe:")
print(dataframe)
print()

# B - Sort the dataframe by TimeZone and State
sorted_dataframe = dataframe.sort_values(by=['TimeZone', 'State'], ascending=[True, True])
print("Sorted Dataframe:")
print(sorted_dataframe)
print()

# C - Add a new column RealPopulation
sorted_dataframe['RealPopulation'] = sorted_dataframe['Population'] * 1000
print("Dataframe with RealPopulation:")
print(sorted_dataframe)
print()

# D - Calculate average, minimum, and maximum population values
average_population = sorted_dataframe['Population'].mean()
min_population = sorted_dataframe['Population'].min()
max_population = sorted_dataframe['Population'].max()
print("Average Population:", average_population)
print("Minimum Population:", min_population)
print("Maximum Population:", max_population)
print()

# E - Calculate the group sum of population for each time zone
group_sum_by_timezone = sorted_dataframe.groupby('TimeZone')['Population'].sum()
print("Group Sum of Population by TimeZone:")
print(group_sum_by_timezone)
print()

# F - Bar plot to show populations
ax = sorted_dataframe.plot.bar(x='State', y='Population', title='Population', rot=0)
ax.set_xlabel('State')
ax.set_ylabel('In Thousands')
plt.show()

# G - Pie plot to show populations
plt.pie(sorted_dataframe['Population'], labels=sorted_dataframe['State'], startangle=90)
plt.title('Population')
plt.show()






#B3-A - Import tips.csv file, filter data, generate histogram, analyze histogram.


# import data 
tips_df = pd.read_csv('C:/Users/artur/Desktop/tips.csv')


# filter tips from males
male_tips = tips_df[tips_df['sex'] == 'Male']['tip']

# histogram
plt.hist(male_tips, bins='auto')
plt.xlabel('Tip Amount')
plt.ylabel('Frequency')
plt.title('Histogram of Tips for Male Customers')
plt.show()

print("The Histogram does not follow a normal distribution. It is asymetrical")
print()



#B3-B - Mean and Standard Deviation of tip amounts. 
mean_tip = male_tips.mean()
std_tip = male_tips.std()

print("Mean Tip Amount:", mean_tip)
print("Standard Deviation of Tip Amount:", std_tip)


