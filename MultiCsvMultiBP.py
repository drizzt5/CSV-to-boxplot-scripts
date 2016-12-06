#!/usr/bin/env python
#
# Program: Take some csv files and spit out boxplots
# Author: Dillon Glasser <dpglasse@nps.edu>
# 
# Usage: python {Program}.py [path] [destination/filename] [optional -x for xaxis label prompts]


import matplotlib.pyplot as plt
import sys
import os
import csv


if __name__ == "__main__":
	assert len(sys.argv) == 3 or len(sys.argv) == 4
	path = sys.argv[1]
	ofile = sys.argv[2]
	fcnt = 0
	bpdata=[]
	xaxisnames=[]
	xtickdefault =[]
	for root, subdirs, files in os.walk(path):
		for filename in sorted(files):
			csvfiles = os.path.join(root, filename)
			if csvfiles.find('.csv') !=-1:
				data=[]
				x = (csvfiles)
				with open(x, 'rb') as f:
					reader = csv.reader(f)
					list1 = list(reader)


				for i in list1:
					data.append(float(i[0]))
				bpdata.append(data)
				fcnt+=1
				xaxisnames.append(x)
			
	if len(sys.argv) == 4: 
		print fcnt
		if sys.argv[3] == "-x":
			for i in range(0, fcnt):
				print xaxisnames[i]
				xaxisnames[i] = raw_input("Enter the axis label: ")
				xtickdefault.append(i+1)	
			plt.xticks(xtickdefault,xaxisnames)
		else:
			print "System Exit: Invalid Command. Must use -x"
			sys.exit()		

	yaxisname = raw_input("Enter the yaxis label: ")	
	plt.ylabel(yaxisname)
	plt.boxplot(bpdata, notch=False, patch_artist=True)
	plt.savefig(ofile)
