#!/bin/env python

# DONE 

"""
Given the string s, produce a list composed of all the 
single characters from the original string
eg:
    s = "Hello"
    becomes
    l = {"H", "e", "l", "l", "o"}
"""
s = "Hi there, my name is Slim"

l = []
for char in s: 
	l.append(char)

print l 