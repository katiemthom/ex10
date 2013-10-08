def round(inp):
    base = int(inp)
    if inp - base >= 0.5:
        return base+1
    else:
        return base
    
def count_lines(inp):
    if not inp:
        return 0
    num = 1

    for c in inp:
        if c == "\n":
           num  += 1    
    return num

def pythagorean_theorem(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    
def reverse(inp):
    ## reverses a list 
    size = len(inp)
    for i in range(len(inp)/2):
        temp = inp[i]
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp
    return inp
    
def word_count():
    ## counts the number of words in a file
    ## and prints them out 
    inp = open("sample_input.txt")
    ws = inp.split()
    h = dict()
    for w in ws:
        num = h.get(w, 0)
        num += 1
        h[w] = num
    
    for k, v in h.iteritems():
        print "%s:\t%d"%(k, v)

def reverse_sort(inp):
    ## sorts least to greatest
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i+1] = inp[i]
                swapped = True

print mystery4([1,2,3,4,5,6])