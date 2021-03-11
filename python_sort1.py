#!/usr/bin/env python

# importing csv module 
import csv 
import collections
import operator
import math

myfile = 'test.csv'
  
# reading csv file 
readcsv = open(myfile,'r') 
name = csv.reader(readcsv,delimiter=',')
next(readcsv)

def loc(x):
	return x[2]
sort = sorted(name,key=loc)

for eachline in sort:
	print eachline

NumOfOrder = collections.Counter()
with open(myfile) as input_file:
    for row in csv.reader(input_file, delimiter=','):
        NumOfOrder[row[2]] += 1
print("Calculate the total number of orders per customer")
print 'Billy Balance: %s' % NumOfOrder['Billy Balance']
print 'Chet Baldry III: %s' % NumOfOrder['Chet Baldry III']
print 'Cody Conroy: %s' % NumOfOrder['Cody Conroy']
print 'Colt Mustang Jr.: %s' % NumOfOrder['Colt Mustang Jr.']
print 'Combo Juarez: %s' % NumOfOrder['Combo Juarez']
print 'Jill Ham: %s' % NumOfOrder['Jill Ham']
print 'Jud Gofferton: %s' % NumOfOrder['Jud Gofferton']
print 'Ken Washington: %s' % NumOfOrder['Ken Washington']
print 'Maria Melendez: %s' % NumOfOrder['Maria Melendez']
print 'Missy Mackle: %s' % NumOfOrder['Missy Mackle']
print 'Roger McHammer: %s' % NumOfOrder['Roger McHammer']
print 'Steve Stevenson: %s' % NumOfOrder['Steve Stevenson']


#with open('test.csv') as handle:
#    reader = csv.reader(handle, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#    float(reader)
#    for row in reader:
#        scores = row[4]
#        average = sum([(score) for score in scores]) / len(scores)
