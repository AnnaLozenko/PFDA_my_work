# Lab Topic 02
# Representing Data
# Author: Anna Lozenko

import csv
import pandas as pd
import numpy as np
import requests

#file data.csv is in the current working directory
with open ("data.csv", "r") as f:
    reader = csv.reader(f, delimiter= ",")
    for line in reader:
        print(line)
    print(type(line))

#this prints out the data line by line as lists of strings



#Deal with header line separately:
with open ("data.csv", "r") as f:
    reader = csv.reader(f, delimiter= ",")
    linecount = 0
    for line in reader:
        #if linecount == 0 (first line, i.e. the header)
        if not linecount:
            #prints the header and separates it from the rest, converts the header into a string 
            print (f"{line}\n=========================")
            #the remaining lines are printed out normally (as lists of strings)
        else:
            print(line)
            #program counts the lines and increases any time it proceeds to the next line, so it can discriminate the header from the rest
        linecount += 1



#calculate the average age. All columns are currently made of strings. 
#import data as Pandas DataFrame
data = pd.read_csv("data.csv", header=0, index_col=0)

#Method 1: without NumPy
age_mean = sum(data["age"])/len(data["age"])
print(age_mean)

#Method 2: with NumPy
age_mean_np = np.mean(data["age"])
print(age_mean_np)



#Read the JSON from Internet
response = requests.get("https://www.gov.uk/bank-holidays.json")
file= response.json()

#output the first holiday in Northern Ireland
print(file["northern-ireland"]["events"][0])
