#!/usr/bin/env python
#
#
#
# 
# ---------------------------------------------------------------------------
# Looking back at this a month later...
#
# Actually, this program is redundant and probably
# every way that I've used this could be accomplished 
# by simply using cat. 
# 
# Example:
# (in a directory with just csv files)
# cat *.csv > [filename.csv]
# This would take all the csv files in some directory, pump them into [filename.csv]
# and probably do a quicker job of it.
#
# And if I needed to get csv files in other directories into my file, 
# cat *.csv >> /path/to/filename.csv
# '>>' should just append to the end of the file.
#
# Dang, but I am learning so it's cool.
# ------------------------------------------------------------------------------
#
#
#
#
#
# Program: Take some csv files and spit out a single csv
# Author: Dillon Glasser <dpglasse@nps.edu>
# 
# Usage: python {Program}.py [path to all the CSV files]
# The program will prompt you for the output filename


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


