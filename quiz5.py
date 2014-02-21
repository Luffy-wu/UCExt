#!/usr/bin/python

import re

"""
Write a regular expression that will match strings that are either all lower case or all upper case.
 Assume that the string is a single word that is at least two letters long and consists only of letters. 
 For example, it will match AM, PM, am or parrot but NOT match Am, aM, Pm or Parrot.

"""
st = "Am AM am aM Pm PM pm pM parrot Parrot PARrot parROT paROTttt "

#print re.findall('\s[A-Z][A-Z]+\s|\s[a-z][a-z]+\s', st)

"""
Write a substitution command that will change names like file1, file2, etc. to file01, file02, etc.
 but will not add a zero to names like file10 or file20.
"""
x = "change file1, file2, file3 ... to file01, file02, not add to file10, file20, file30"
#answer = re.sub("file\d{1}\D","XXX", x) # XX XXX XXXetc. to file01, file02, file10, file20
#answer = re.findall("(file)(\d{1}\D)", x) # [('file', '1,'), ('file', '2,')]
#answer = re.findall("file(\d{1}\D)", x) # [('file', '1,'), ('file', '2,')]

pattern = re.compile(r"file(\d{1}\D)")
print pattern.sub(r"file0\1", x)


"""
Many news and mail readers automatically highlight URLs that appear in text, for example
 http://yahoo.com or www.msnbc.com. Construct a regular expression that will extract the
  names of URLs embedded in a string.
"""
webstr = "i like to read yas@gskjd http://yahoo.com and  wewww www.msnbc.com is that cool"

#webpattern = re.compile(r'\w+@\w+.\w+')
# webpattern = re.compile(r'(\w+://\w+.\w+|\w+w\.\w+.\w+\.\w+)')
webpattern = re.compile(r'(\w+://\w+.\w+|\b..w\.\w+.\w+\.\w+)')
print webpattern.findall(webstr)

"""
Write a function that takes times of the form 03:12:19 (in other words, three hours, 
twelve minutes, and nineteen seconds) and converts them to the corresponding number of seconds
"""

