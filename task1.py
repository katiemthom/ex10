#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]

for i in range(len(l)):
	for j in range(i, len(l)):
		if l[j] > l[i]: 
			l.insert(i, l[j])
			del l[j+1]
			
print l 
