# DONE 

"""
Given a multiline string 's', 
print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""

s = "Sorry,\nMy people need me\nI must go"
l = s.split("\n")

for i in range(len(l)): 
	print str(i + 1) + ". " + l[i]