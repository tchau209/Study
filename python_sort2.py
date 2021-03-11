#!/usr/bin/env python

# importing csv module 
import csv 
import operator

file = 'out.txt'
# reading csv file 
readcsv = open(file,'r') 
name = csv.reader(readcsv,delimiter=',')
#next(readcsv)

def loc(x):
	return x[2]
sort = sorted(name,key=loc)

for eachline in sort:
	print eachline


