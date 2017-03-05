#!/bin/python3

import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
mylist = [a,b,c,d,e]
maxsum = sum(mylist)-min(mylist)
minsum = sum(mylist)-max(mylist)
print(minsum,maxsum)
