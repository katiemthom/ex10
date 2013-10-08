#!/bin/env python

# DONE

"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""

d = {"q": 5, "m": 3, "z":2, "a": 10}

l = d.items()

s_l = sorted(l)

for item in s_l:
	print str(item[0]) + ", " + str(item[1])