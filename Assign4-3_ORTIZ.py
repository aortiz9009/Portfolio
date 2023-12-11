# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 23:54:52 2023

@author: artur
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

# Set the number of random numbers to be generated
num_random_numbers = 100

# Generate random numbers
random_numbers = np.random.uniform(low=0, high=15, size=num_random_numbers)

# Create a histogram to visualize the frequency distribution
plt.hist(random_numbers, bins='auto', alpha=0.9, rwidth=0.90)
plt.title('Frequency Distribution of Expected Waiting Time')
plt.xlabel('Expected Waiting Time (minutes)')
plt.ylabel('Frequency')
plt.show()

# Test the distribution using Kolmogorov-Smirnov test
test_statistic, p_value = kstest(random_numbers, 'uniform')
alpha = 0.05  # significance level

# Interpret the results
if p_value > alpha:
    print("The distribution of expected waiting time follows a uniform distribution.")
else:
    print("The distribution of expected waiting time does not follow a uniform distribution.")
    

