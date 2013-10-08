#!/bin/env python

# DONE

"""
Given list l1 and list l2, produce list l3 
that contains the contents of both lists, 
removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""

l1 = [1, 3, 4, 6, 8, 10]
l2 = [93, 2, 23, 77, 66, 1]

def combine(l1, l2): 
	l3 = l1 + l2
	l4 = []
	for val in l3: 
		if val not in l4: 
			l4.append(val)
	return l4

print combine(l1, l2)