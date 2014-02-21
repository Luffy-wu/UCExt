#!/usr/bin/python

import re

"""
Write a regular expression that will match strings that are either all lower case or all upper case.
 Assume that the string is a single word that is at least two letters long and consists only of letters. 
 For example, it will match AM, PM, am or parrot but NOT match Am, aM, Pm or Parrot.

"""

# CASE 1
st = "Am AM am aM Pm PM pm pM parrot PARROT  Parrot PARrot parROT paROTttt "
print "Problem 1: "
print "test string: " + st
print re.findall(r'\b([A-Z][A-Z]+|[a-z][a-z]+)\b', st)

"""
Write a substitution command that will change names like file1, file2, etc. to file01, file02, etc.
 but will not add a zero to names like file10 or file20.
"""

original = "change file1, file2, file3 ... to file01, file02, not add to file10, file20, file30"
print "\nProblem 2:"
pattern = re.compile(r"file(\d{1}\D)")
print original
print pattern.sub(r"file0\1", original)


"""
Many news and mail readers automatically highlight URLs that appear in text, for example
 http://yahoo.com or www.msnbc.com. Construct a regular expression that will extract the
  names of URLs embedded in a string.
"""
webstr = "i like to read http http://yahoo.com  https://weather.com and  www. www.msnbc.com www.google.com is that cool"

#webpattern = re.compile(r'\w+@\w+.\w+')
# webpattern = re.compile(r'(\w+://\w+.\w+|\w+w\.\w+.\w+\.\w+)')
#webpattern = re.compile(r'(\w+://\w+.\w+|\b..w\.\w+.\w+\.\w+)')
#print webpattern.findall(webstr)
print "\nProblem 3:"
print "test string: " + webstr
webs = re.findall(r"http\w?://\w+.\w+|\swww.\w+.\w+", webstr)
print webs


"""
Write a function that takes times of the form 03:12:19 (in other words, three hours, 
twelve minutes, and nineteen seconds) and converts them to the corresponding number of seconds
"""

def convertToSeconds(string):
    hhmmss = string.split(":") #split to get each unit separately
    total = (int(hhmmss[0]) * 60 * 60) + (int(hhmmss[1]) * 60) + int(hhmmss[2])
    return total

time = "03:12:19"
print "\nProblem 4:\n%s is %d seconds total " % (time, convertToSeconds(time))
