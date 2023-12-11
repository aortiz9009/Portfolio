# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:33:38 2023

@author: artur
"""
print("B-1---------------------------------------------------------")

def calculate_sales_tax(purchase_amount):
    state_tax_rate = 0.05
    county_tax_rate = 0.025

    state_tax = purchase_amount * state_tax_rate
    county_tax = purchase_amount * county_tax_rate
    total_tax = state_tax + county_tax
    total_amount = purchase_amount + total_tax

    return state_tax, county_tax, total_tax, total_amount

# Get the purchase amount from the user
purchase_amount = float(input("Enter the purchase amount: "))

# Calculate sales tax and total amount
state_tax, county_tax, total_tax, total_amount = calculate_sales_tax(purchase_amount)

# Display the results
print("Purchase amount:", purchase_amount)
print("State sales tax:", state_tax)
print("County sales tax:", county_tax)
print("Total sales tax:", total_tax)
print("Total sale amount:", total_amount)
print("------------------------------------------------------------")











print("B-2----------------------------------------------------")

tuition = 5333  # Initial tuition amount
rate_increase = 0.03  # Tuition increase rate (3% per year)

for year in range(1, 6):
    tuition += tuition * rate_increase  # Calculate the new tuition amount
    print(f"Year {year}: ${tuition:.2f}")
print("----------------------------------------------------")
  
    
    
 
    
 
    
print("B-3-----------------------------------------------------")
 
 
numbers = []

# Prompt the user to enter numbers
for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

# Find the lowest number
lowest = min(numbers)

# Find the highest number
highest = max(numbers)

# Calculate the total sum of the numbers
total = sum(numbers)

# Calculate the average of the numbers
average = total / len(numbers)

# Display the results
print("Data analysis:")
print(f"Lowest number: {lowest}")
print(f"Highest number: {highest}")
print(f"Total sum: {total}")
print(f"Average: {average}")


print("---------------------------------------------------------")


#B-4

import seaborn as sns

# Load  dataset from seaborn
titanic_data = sns.load_dataset('titanic')

# SAC approach using groupby and filter groups with average age < 30
filtered_groups = titanic_data.groupby('class').filter(lambda x: x['age'].mean() < 30)

# Display the data from the filtered groups
for class_name, group_data in filtered_groups.groupby('class'):
    print(f"Class: {class_name}")
    print(group_data)
    print()
    
    
 #B-5   
 
size = 12

# Draw the tree
for i in range(size):
    # Print spaces before the asterisks
    for _ in range(size - i - 1):
        print(" ", end="")
    
    # Print asterisks
    for _ in range(2 * i + 1):
        print("|", end="")
    
    # Move to the next line after each row
    print()

# Draw the base of the tree
for _ in range(size - 1):
    print(" ", end="")
print("|")

# Draw the star
for _ in range(size - 1):
    print(" ", end="")
print("star")









  

















    





