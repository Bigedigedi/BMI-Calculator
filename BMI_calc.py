#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In[ ]:

"""
usage: BMI_calc.py size in cm weight in kg

"""

size = float(input("Please give your size in cm"))
weight = float(input("Please give your weight in kg"))

def bmi_calc(size,weight):
    size_in_m = size/100
    bmi = weight/(size_in_m**2)
    
    if bmi < 18.5:
        print("Your BMI is",round(bmi,1),".You are Underweight")
    elif bmi < 25:
        print("Your BMI is",round(bmi,1),".You are normalweight")
    elif bmi < 30:
        print("Your BMI is",round(bmi,1),".You are overweight")
    else:
        print("Your BMI is",round(bmi,1),".You have adipositas")

bmi_calc(size,weight)

