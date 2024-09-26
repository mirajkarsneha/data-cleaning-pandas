{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

#Functions
import re
import pandas as pd
import numpy as np

#remove the word "Reported" and keep the date
def clean_dates(input_string):
    input_data = str(input_string)
    cleaned_string = re.sub(r'Reported\s*', '', input_data)
    return cleaned_string 
    
#Replace two numbers which has & with average result of two numbers
def clean_year_column(input_string):
    input_data = str(input_string)
    return re.sub(r'(\d{4})\.0', r'\1', input_data)

def replace_with_average(age_str):
    # Regex to find "x & y"
    age_str = str(age_str) 
    match = re.match(r'(\d+)\s*(?:and|or|to|&|/)\s*(\d+)', age_str)
    
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        average = (num1 + num2) / 2
        return average
    return age_str

#Find all numbers (including decimals) in the string
def extract_numbers(value):
    value = str(value).strip()
    numbers = re.findall(r'\d+(?:\.\d+)?', value)
    
    if numbers:
        return int(round(float(numbers[0])))
    return np.nan

#remove ½ and round up the numbers
def clean_age(age_str):
    age_str = str(age_str).strip()
    match = re.findall(r'\d+\.?\d*|\d+½', age_str)
    
    if match:
        processed_numbers = []
        for num in match:
            if '½' in num:
                num = num.replace('½', '.5') #Eg. 6½ is round up as 6.5
            processed_numbers.append(float(num))
        processed_numbers = [num for num in processed_numbers]
        
        if processed_numbers:
            return sum(processed_numbers) / len(processed_numbers)
    
    return None

#Keep sex/gender as F and M and replace other with empty value
def clean_gender_column(input_string):
    input_str = str(input_string)
    return re.sub(r'[^FM]', '', input_str)

#Keep name replace female|nan|NaN with empty value
def remove_female_and_nan(input_string):
    input_string = str(input_string)
    cleaned_str = re.sub(r'\b(male|female|nan|NaN)\b', '', input_string, flags=re.IGNORECASE)
    cleaned_str = re.sub(r'\s*,\s*', ',', cleaned_str)  
    cleaned_str = re.sub(r',+', ',', cleaned_str)       
    cleaned_str = cleaned_str.strip(', ')
    return cleaned_str