'''
Created on Dec 30, 2017

@author: alireza
'''
import math
li = [-10, 2, -3, 4, -5, 9]
si = sorted(li, key=abs)
li.sort(reverse=True)
print li
print si