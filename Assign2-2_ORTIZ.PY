# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 22:49:00 2023

@author: artur
"""
#Tax and assessment value calculations
def calculate_tax(val):
    actual_value = 0.6*val
    property_tax = 0.0072*actual_value
    showPropertTax(actual_value,property_tax) 
    
# Property tax and assessment value displayed    
def showPropertTax(ass_value,p_tax):
    print('Assessed value:'+'$'+str(round(ass_value,4)))
    print('property tax: '+ '$'+ str(round(p_tax,4)))

# User enters property value
actual_value=float(input('Enter the actual value:')) 


calculate_tax(actual_value)