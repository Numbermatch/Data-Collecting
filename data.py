import numpy as np
import pandas as pd
import os
import re
import csv

directory = './Man_Notes/'
directory2 = './'
ourDict = {}

#Constructing our Dictionary of Columns
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	
	with open(f, 'r') as file:
		data = file.read().replace('\t', '')
		string_lines = data.split("\n")
	
		for line in string_lines:
			if line.isupper() and line[0] != " ":
				key_word = line
				
				if key_word not in ourDict:
					ourDict[key_word] = 1
				else:
					ourDict[key_word] += 1

#Filtering our Dictionary for relevant columns
for vali in list(ourDict):
	if ourDict[vali] <= 10:
		del ourDict[vali]

ourDict["Path"] = ""
final_df = pd.DataFrame([ourDict])

#Looping through to construct a pandas dataframe
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	with open(f, 'r') as file:
		print(f)
		for vali in list(ourDict):
			ourDict[vali] = ""
		
		ourDict["Path"] = f
		data = file.read().replace("\t", "")
		string_lines = data.split("\n")
		
		key_word = "NAME"
		for line in string_lines:

			if line.isupper() and line[0] != " ":
				key_word = line
			if key_word in ourDict:
				ourDict[key_word] += line.replace(key_word, "")
	
	current_df_item = pd.DataFrame([ourDict]).copy()
	final_df = pd.concat([final_df, current_df_item]).copy()

#Modification & writing out file
final_df = final_df.iloc[1: , :]
final_df.to_csv(directory2 + "data_dump.csv")
