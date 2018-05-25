'''
Created on May 15, 2018

@author: mkhan
'''
import csv
f_ptr = open("sample.csv", "r")
reader = csv.DictReader(f_ptr)

for row in reader:
    print(row['year'], row['headcount'])


for lines in reader:
    print(lines)

f_ptr.close()