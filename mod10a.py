#!/usr/bin/python

"""
Python provides several modules to allow you to easily extend some of the basic objects in the language. 
Among these modules are UserDict, UserList, and UserString. (Refer to the chart in Topic 10.3 to see 
    what the methods you need to override look like.)

Using the UserDict module, create a class called Odict, which will be just like a dictionary but will 
"remember" the order in which key/value pairs are added to the dictionary. (Hint: Override the built-in 
    __setitem__ method.) Create a new method for the Odict object called okeys, which will return the ordered keys. 

Using the UserList module, create a class called Ulist, and override the __add__, append, and extend 
methods so that duplicate values will not be added to the list by any of these operations.

"""

import UserDict
import UserList

class Odict(UserDict.UserDict):
    def __init__(self, data = {}, **kw):
        UserDict.UserDict.__init__(self)
        self.update(data)
        self.update(kw)
        self.keylist = []

    def __setitem__(self,key,value):
        self.data[key] = value
        self.keylist.append(key)

    def okeys(self):
        return self.keylist


myDict = Odict()
myDict['d'] = 'value5'
myDict['a'] = 'value4'
myDict['e'] = 'value6'

print myDict.okeys()


class Ulist(UserList.UserList):
    def __init__(self, data = [], **kw):
        UserList.UserList.__init__(self)
        self.data = data

    def __add__(self, newvalue):
        for item in newvalue:
            if item in self.data:
                print "%r already exists, not adding." % item
            else:
                self.data += [item]
        return self.data

    def append(self,newvalue = None):
        if newvalue in self.data:
            print "%r already exists, not adding." % newvalue
        else:
            return self.data.append(newvalue)

    def extend(self, newvalue = []):
        for item in newvalue:
            if item in self.data:
                print "%r already exists, not adding." % item
            else:
                return self.data.extend(item)
        return self.data

mylist = Ulist([1,2,3])
#mylist.__add__([5,6])
#mylist.append('a')
#mylist.append([3])
#mylist.extend([1,2,3,'a'])
print mylist