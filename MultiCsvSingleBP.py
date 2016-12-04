#!/usr/bin/env python
#
# Program: Take some csv files and spit out boxplots
# Author: Dillon Glasser <dpglasse@nps.edu>
# 
# Usage: python {Program}.py [path] [destination/filename] [optional x axis name]


import matplotlib.pyplot as plt
import sys
import os
import csv


if __name__ == "__main__":
	assert len(sys.argv) == 3 or len(sys.argv) == 4
	path = sys.argv[1]
	ofile = sys.argv[2]
	if len(sys.argv)==4:
		xlbl = sys.argv[3]
	else:
		xlbl = 1

	data=[]
	
	for root, subdirs, files in os.walk(path):
		for filename in sorted(files):
			csvfiles = os.path.join(root, filename)
			if csvfiles.find('.csv') !=-1:
				x = (csvfiles)
				with open(x, 'rb') as f:
					reader = csv.reader(f)
					list1 = list(reader)


				for i in list1:
					data.append(float(i[0]))


	plt.ylabel('Percentage of Paths with ICMPext')
	plt.boxplot(data, notch=False, patch_artist=True)
	plt.xticks([1], [xlbl])
	plt.savefig(ofile)
