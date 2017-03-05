#!/bin/python

import sys

def lonely_integer(a):
    if len(a)==1:
        return a[0]
    else:
        mydict = {}
        for num in a:
            if num in mydict.keys():
                mydict[num] = mydict[num]+1
            else:
                mydict[num] = 0
        return mydict.keys()[mydict.values().index(0)]
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)