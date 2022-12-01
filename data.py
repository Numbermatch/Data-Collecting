import numpy as np
import pandas as pd
import os
import re
import csv

directory = '/home/paul/Documents/Machine_Learning/Bash_Predictions/Man_Notes/'
directory2 = '/home/paul/Documents/Machine_Learning/Bash_Predictions/'
ourDict = {}

#Constructing our Dictionary of Columns
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	
	with open(f, 'r') as file:
		data = file.read().replace('\t', '')
		string_lines = data.split("\n")
	
		for line in string_lines:
			#if line.split(" ")[0].isupper():
			if line.isupper() and line[0] != " ":
				#key_word = line.split(" ")[0]
				key_word = line
				
				if key_word not in ourDict:
					ourDict[key_word] = 1
				else:
					ourDict[key_word] += 1

ourURL = "/home/paul/Documents/Machine_Learning/Bash_Predictions/Man_Notes/lsb_release.txt"

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
		#data = data.replace("SEE ALSO", "SEE_ALSO")
		string_lines = data.split("\n")
		
		key_word = "NAME"
		for line in string_lines:

			#if line.split(" ")[0].isupper():
			if line.isupper() and line[0] != " ":
				#key_word = line.split(" ")[0]
				key_word = line
			if key_word in ourDict:
				ourDict[key_word] += line.replace(key_word, "")
	
	
	current_df_item = pd.DataFrame([ourDict]).copy()
	if f == ourURL:
		with open('testcsv.csv', 'w') as ourW:
			w = csv.DictWriter(ourW, ourDict.keys())
			w.writeheader()
			w.writerow(ourDict)
		samplingdf = ourDict.copy()
	#final_df = final_df.append(current_df_item, ignore_index=True)
	
	final_df = pd.concat([final_df, current_df_item]).copy()
	#break

for val in samplingdf:
	print(val, ":", samplingdf[val])

#Modification & writing out file
final_df = final_df.iloc[1: , :]

#final_df.to_csv(directory2 + "data_dump.csv")

