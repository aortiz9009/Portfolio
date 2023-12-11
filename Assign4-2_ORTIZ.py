# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 23:13:30 2023

@author: artur
"""

import seaborn as sns
import matplotlib.pyplot as plt

# A Import "titanic" dataset and display the first five observations
titanic_data = sns.load_dataset('titanic')
print(titanic_data.head())

# B Group survivors by class and town of embarkation and visualize using barplot
sns.barplot(x='class', y='survived', hue='embark_town', data=titanic_data, palette=['red', 'blue', 'green'])
plt.title('Survivors by Class and Town Embarkment')
plt.xlabel('Class')
plt.ylabel('Survival Rate')
plt.show()

# C Import "iris" dataset and display pairwise relationships using pairplot
iris_data = sns.load_dataset('iris')
sns.pairplot(iris_data)
plt.show()

# D Change plot types for non-diagonal comparisons and specify histogram for diagonal plots
sns.pairplot(iris_data, diag_kind='hist', kind='scatter')
plt.show()
