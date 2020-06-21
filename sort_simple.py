#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:31:32 2020

@author: samuelchotzen
"""


import pandas as pd

sheet_to_sort = input("Provide the path to the spreadsheet you'd like to clean up: ")
split_path = sheet_to_sort.split('/')
file_name = split_path[-1]
df=pd.read_excel(sheet_to_sort)
order = input("Would you like to sort "+file_name+" in ascending (A) or descending (D) order? ")
print("") 
columns = df.columns.ravel()
columns_clean = []
for col in columns:
    columns_clean.append(col)
print(file_name," contains the following types: ", columns_clean)
index = input("Enter one of the column names listed above to declare the sorting index: ")
if order == "A":    
    df=df.sort_values(index, ascending=[True])
    order_str = "ascending order"
else:
    df=df.sort_values(index, ascending=[False])
    order_str = "descending order"
overwrite = input("Would you like to overwrite "+file_name+" with the sorted version? (Y/N) ")
if overwrite == "Y":
    df.to_excel(sheet_to_sort)
    print("")
    print(file_name+" has been sorted by "+index+" in "+order_str)
else:
    new_path = input("Provide a preferred path to the sorted copy of "+file_name+": ")
    df.to_excel(new_path)
    print("")
    print(file_name+" has been sorted by "+index+" in "+order_str+" and is output under "+new_path)