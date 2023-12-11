# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 22:39:51 2023

@author: artur
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'CityA_High': [38, 50, 60, 71, 78, 79, 75, 67, 56, 44, 37, 33],
    'CityA_Low': [24, 35, 42, 53, 60, 62, 57, 47, 38, 28, 22, 19],
    'CityB_High': [55, 63, 75, 84, 94, 93, 91, 83, 76, 67, 59, 54],
    'CityB_Low': [28, 36, 48, 59, 67, 69, 65, 56, 46, 37, 30, 26]
}

df = pd.DataFrame(data)

df_cityA = df[['CityA_High', 'CityA_Low']]

# Line plot for City A temperatures
ax = df_cityA.plot.line(title='City A Temperature Line Plot', color=['red', 'blue'])
ax.set_ylabel('Temperature')
ax.set_xlabel('Month')
plt.show()

# Bar plot for City A high and low temperatures
X = np.arange(12)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(X - 0.125, df_cityA['CityA_High'], color='red', width=0.25)
ax.bar(X + 0.125, df_cityA['CityA_Low'], color='blue', width=0.25)
ax.set_title('City A High Temperature vs Low Temperature')
ax.set_ylabel('Temperature')
ax.set_xlabel('Month')
ax.set_xticks(X)
ax.set_xticklabels(range(1, 13))
ax.legend(labels=['High', 'Low'])
plt.show()

# Scatter plot comparing City A and City B temperatures
plt.scatter(df['CityA_High'], df['CityB_High'], label='High', color='red')
plt.scatter(df['CityA_Low'], df['CityB_Low'], label='Low', color='blue')
plt.legend()
plt.xlabel('City A')
plt.ylabel('City B')
plt.title('City A vs City B Scatter Plot')
plt.show()

    