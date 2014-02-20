#!/usr/bin/python

"""
Suppose you want to determine whether an arbitrary text string can be converted to a number. 
Write a function that uses a try/except clause to solve this problem. Can you think of another 
way to solve this problem?
"""

def convertMe(string):
    try:
        number = int(string)
        print "converted %s to %d" % (string, number)
    except ValueError:
        print("%r cannot be converted to an integer.") % (string)


convertMe("4ssss")
convertMe("-745")

#alternate solution

def convertMe2(string):
    if string.isdigit():
        number = int(string)
        print "converted %s to %d" % (string, number)
    else:
        print("%r cannot be converted to an integer.") % (string)

convertMe2("dfdf7 8s")
convertMe("-85")

"""
The input function will read a single line of text from the terminal. If you wanted to read several 
lines of text, you could embed this function inside a while loop and terminate the loop when the user 
of the program presses the interrupt key (Ctrl-C under UNIX, Linux and Windows.) Write such a program, 
and note its behavior when it receives the interrupt signal. Use a try/except clause to make the program 
behave more gracefully.

"""
import sys

def readtext():
    moretext = raw_input("enter some text! ")
    try:
        while True:
            text = raw_input("enter more text!!! (hit ctl+c to exit.)")
            moretext += text
            print moretext
    except KeyboardInterrupt:
        print "\nGot interrupt, exiting program...\n"
        sys.exit()

readtext()
