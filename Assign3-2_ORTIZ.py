# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:19:14 2023

@author: artur
"""


import pandas as pd
import numpy as np

athlete = pd.read_csv("C:/Users/artur/OneDrive/ISQS 6337/Athlete (1).csv")

df = pd.DataFrame(athlete)

print("First 5 rows of dataframe:")
print(df[:5])
print()

array = np.array(df)
rows, columns = array.shape

df.at[0, "Year"] = 1993

print("Year column:")
print(df["Year"])
print()

df["Weight"] -= 10

print("Weight column:")
print(df["Weight"])
print()

df["Height/Weight"] = df["Height"]/df["Weight"]
print("DataFrame:")
print(df)


