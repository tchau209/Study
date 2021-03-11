#!/usr/bin/env python

# importing csv module 
import csv 

filename = 'test.csv'
rowprice = 0
total = 0

#with open('test.csv') as csvfile:
# data = csv.DictReader(csvfile)
# print("Customer Name 	Price")
# print("---------------------------------")
# for row in data:
#   print(row['Customer Name'], row['Price'])

with open('test.csv') as csvfile:
 data = csv.DictReader(csvfile)
# print("Price")
# print("-------------")
 for row in data:
   s = row['Price']

   #original_stdout = sys.stdout # Save a reference to the original standard output
   #with open('nodollarsign.txt', 'w') as f:
   #	sys.stdout = f
   #     print(s.replace('$', ''))
   #     sys.stdout = original_stdout

   print(s.replace('$', '')) 
#   rowprice = float(s)
   #total = total + rowprice
#   print (total)

