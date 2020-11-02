# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:42:58 2020

@author: Yung
"""
def test():
    print("Hello World")

# Run this functions with apply on the education column
# Input: int values from 0-6
# Output: 4 if value is 0, 5, or 6 else value
def clean_education_col(value):
    if value in [0, 5, 6]:
        return 4
    else:
        return value

# Run this functions with apply on the marital_status column
# Input: int values from 0-3
# Output: if the value is not 1, 2, or 3, set it as 3. 
def clean_marital_status(value):
    if value not in [1, 2, 3]:
        return 3
    else:
        return value
    
def clean_pay_status(value):
    if value <= 0:
        return 0
    else:
        return value