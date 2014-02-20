#!/usr/bin/python

"""
1. Write a function that accepts the name of a file and returns a tuple containing the number of lines, words, 
and characters that are in the file. (Hint: Use the split function of the string module to help you count 
the words in the file.). """


def filecounts(filename):
    try: 
        f = open(filename) 
    except IOError, e: 
        print("Unable to open file for reading %s: %s" % (filename, e))

    text = f.readlines()
    f.close()

    # let's count letters, words, and lines
    linecounter = wordcounter = lettercounter = 0

    for item in text:
        lettercounter += len(item)
        wordcounter += len(item.split())
        linecounter += 1

    return lettercounter, wordcounter, linecounter



print "Problem 1: letters: %d, words: %d, lines: %d" %  (filecounts("./short.txt"))
#confirm asnwer with wc:
#% wc short.txt 
#      50     202    1224 short.txt
#

"""
2. Write a function that accepts an arbitrary number of lists and returns a single list with exactly one 
occurrence of each element that appears in any of the input lists. 
"""

def listMerge(*args):
    all_lists = []
    for item in args:
        if not isinstance(item, list):
            item = [item]
            all_lists += item
        else:
            all_lists += item
    
    return list(set(all_lists))


print  "\nProblem 2:", listMerge([1,2,3,4], [7,4,7,8], [9,3], "text")


"""
3. Use the map function to add a constant to each element of a list. Perform the same operation using 
a list comprehension. 

"""
xlist = [4,2,-9,32,0]
print "\nProblem 3:"
print "add 2 to each number in this list: ", xlist
print "using map: ", map(lambda x:x+2, xlist) 
print "using listcomp:", [x+2 for x in xlist]


"""
4. Write a function that combines several dictionaries by creating a new dictionary with all the keys
 of the original ones. If a key appears in more than one input dictionary, the value corresponding to 
 that key in the new dictionary should be a list containing all the values encountered in the input 
 dictionaries that correspond to that key.
"""

d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}
d3 = {"m": 35, "x": 4}

def dictMerge(*args):
    args_list = list(args)
    dicts_list = []
    all_keys = []

    for item in args_list: #combine all keys into a list
        if isinstance(item, dict):
            all_keys += item.keys()
            dicts_list.append(item) #get a list of dictionaries from all args

    result_dict = {}
    for item in all_keys: #make an empty list for each key
        if not result_dict.get(item): 
            result_dict[item] = []

    for dictx in dicts_list: #populate the dict of empty lists with keys and values
        for key, value in dictx.items(): #populate the dict of empty lists with keys and values
            result_dict[key] += [value]
    return result_dict

print "\nProblem 4:", dictMerge(d1,"stuff",d2,45,d3)
