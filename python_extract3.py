#!/usr/bin/env python

# importing csv module 
import csv 

entries = []
duplicate_entries = []
with open('test.csv', 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        if columns[2] not in entries:
            entries.append(columns[2])
        else:
            duplicate_entries.append(columns[2]) 

if len(duplicate_entries) > 0:
    with open('out.txt', 'w') as out_file:
        with open('test.csv', 'r') as my_file:
            for line in my_file:
                columns = line.strip().split(',')
                if columns[2] in duplicate_entries:
                   # print line.strip()
                    out_file.write(line)
else:
    print "No repetitions"

print("Organize and sort the data by customer name")
execfile("python_sort1.py")
print("Calculate the average cost of orders per customer")
execfile("python_sort2.py")
execfile("python_extract2.py")

