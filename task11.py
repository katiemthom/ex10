#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it 
according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""

def title(my_title):
    l = my_title.split()
    l[0] = chr(ord(l[0][0]) - 32) + l[0][1:]
    title = ""
    title += l[0]
    for word in l[1:]: 
    	if word not in ["a", "an", "the", "of"]: 
    		word = chr(ord(word[0]) - 32) + word[1:]
    	title += " "
    	title += word
    return title 

print title("a tale of two cities")

