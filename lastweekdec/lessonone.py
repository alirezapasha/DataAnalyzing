'''
Created on Dec 30, 2017

@author: alireza
'''
#import packages
import csv
from pandas.compat import FileNotFoundError


#declare constants
DATABASE_PATH = '/home/Alireza/Work/DataBase/bitcoin_one_year.csv' 
count = 0

#loading a file
try:    
    with open(DATABASE_PATH, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader :
#             print line
            count += 1
         
    print count
    
except FileNotFoundError as e:
    print "an Exception happen during get the file ", e
except Exception:
    print "something wrongs"
    
def add(a, b):
    return a+b
