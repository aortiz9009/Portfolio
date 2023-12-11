# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:47:38 2023

@author: artur
"""
#A.
import numpy as np
import pandas as pd 

#B.
id= ["a", "b", "c","d", "e", "f","g", "h", "i","j"]

exam_scores = {
 "name": ["Yuan", "David", "Margaret",
      "Daniel", "Gina", "Catherene",
      "Chris", "Jaeki","Ethan","Murphy"],

 "score": [12.5, 9, 16.5, 'N/A',9,20,14.5,'N/A',
       8, 19],

 "attempt": [1,3,2,3,2,3,1,1,2,1],
 "pass/fail":["Yes", "No", "Yes","No","No","Yes","Yes",
      "No","No","Yes"]}

df = pd.DataFrame(exam_scores,index=id)


print(df)

#D.
label1 = df.loc[['a', 'b', 'e','f' ], ["name", "score"] ]


#E.
attemptgreaterthan2=df.loc[df['attempt'] > 2]


df.replace('N/A', np.NaN, inplace = True)
attemptNA = df.loc[ df.isnull().any(axis = 1)]


attemptgreaterthan2 = df.loc[ (df['attempt'] > 2) &
df.isnull().any(axis = 1) ]
df.replace(np.NaN, 'N/A', inplace = True)


#F
df.loc["k"] = [ "Song", 15.5, 1, "Yes" ]
print(df)

df.drop(['h'], inplace=True)



#G.
df.replace("Yes", "Pass" , inplace=True)
df.replace("No", "Fail", inplace = True )


