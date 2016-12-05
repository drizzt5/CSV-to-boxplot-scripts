#!/usr/bin/env python
#
# Program: Take some csv files and spit out boxplots
# Author: Dillon Glasser <dpglasse@nps.edu>
# 
# Usage: python {Program}.py [path] [destination/filename] [optional x axis name]


import sys
#import os
import csv


if __name__ == "__main__":
	csvdata = []
	path = []
	data = []
	for i in range(1,len(sys.argv)):
		path = sys.argv[i]
		with open(path, 'rb') as f:
			reader = csv.reader(f)
			csvdata = list(reader)
		for i in csvdata:
			data.append(float(i[0]))
	
	
	output = raw_input("Enter the output filename: ")
	with open(output, 'wb') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter ='\n')
		csvwriter.writerow(data)


