# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Enter number of seconds
seconds = float(input('Enter number of seconds: '))
print('Here is the time in Hours, Minutes, and Seconds')

# Number of hours
hours = seconds// 3600
print('Hours:', hours)

# Number of minutes
minutes = (seconds // 60) % 60
print('Minutes:', minutes)

# Number of seconds
seconds = seconds % 60
print('Seconds:', seconds)


speed = int(input("What is the speed of the vehicle in mph? "))

while(speed<0 or speed>120):
    speed = int(input("Invalid input. What is the speed of the vehicle in mph? "))

hours = int(input("How many hours has it traveled? "))

while(hours<0 or hours>100):
    hours = int(input("Invalid input. How many hours has it traveled? "))

print("{:<6} {:<20}".format("Hours", "Distance Traveled"))
