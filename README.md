# CSV-to-boxplot-scripts
Here are some short scripts that will take CSV files and turn them into simple box plots.

I wrote these scripts for a project that required a lot of box plots. They are hacked together, but they work. I gave some basic syntax for usage in the header of each file. 

Just edit the ylabel in the program if you need to change it.




* MultiCsvMultiBP.py

-Will look through directory it is pointed to, take multiple CSVs, and spit them out onto seperate box plots. The -x option will allow you to change the xaxis label of each box plot. (optional, will default to numbers)

* MultiCsvSingleBP.py

-Will look through directory, take multiple CSVs, and spit them onto a single boxplot. sys.argv[4] will be the xaxis name (optional, defaults to 1)

* SingleCsv.py

-Point it to a single csv and it will make a single boxplot. sys.argv[4] will be the xaxis name (optional, defaults to 1)
