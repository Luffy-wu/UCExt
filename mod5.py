#!/usr/bin/python
#humera yasmin khan X442.3 Assignment 5.

"""
1. Using the keys method for dictionaries and the sort method for lists, write a for loop 
that prints the keys and corresponding values of a dictionary in the alphabetical order of the keys.
"""

phonebook = { 'Fred':'555-1231','Andy':'555-1195','Sue':'555-2193', 'Mary':'555-3214' }

nameslist = phonebook.keys()
nameslist.sort()

print "Problem 1:"
for i in nameslist:
    print i, phonebook[i]

"""
2. As an alternative to the range function, some programmers like to increment a counter inside a while 
loop and stop the while loop when the counter is no longer less than the length of the array. Rewrite 
the following code using a while loop instead of a for loop.

a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [] 
for i in range(len(a)): 
    big.append(max(a[i],b[i])) 
print big
[9, 14, 9, 14, 15, 18, 15]
"""

a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 

big = []
i = 0
while i < len(a):
    big.append(max(a[i],b[i]))
    i += 1

print "\nProblem 2:", big

"""
3. Write a loop that reads each line of a file and counts the number of lines that are read until
 the total length of the lines is 1,000 or more characters. Use a break statement to make sure that 
 you don't continue reading the file once at least 1,000 characters are read.

"""
filename = './short.txt' 
try: 
    f = open(filename) 
except IOError: 
    print("Can't find %s" %  filename)

text = f.readlines()
f.close()

lettercounter = 0
linecounter = 0
for item in text:
    linecounter += 1
    lettercounter += len(item)
    if lettercounter >= 1000:
        break

print "\nProblem 3:", linecounter, lettercounter

"""
4. Modify the program written in question 3 so that it
doesn't count characters on any line that begins with a pound sign (#).
"""


filename = './short.txt' 
try: 
    f = open(filename) 
except IOError: 
    print("Can't find %s" %  filename)

text = f.readlines()
f.close()

lettercounter = 0
linecounter = 0
for item in text:
    if item[0] != "#":
        linecounter += 1
        lettercounter += len(item)
        if lettercounter >= 1000:
            break


print "\nProblem 4:", linecounter, lettercounter
