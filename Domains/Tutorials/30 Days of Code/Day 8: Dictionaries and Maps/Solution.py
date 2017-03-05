#!/usr/bin/python
import sys
mydict = {}
n = int(raw_input())
for i in range(n):
    line = raw_input().split()
    mydict[line[0]]=line[1]
for line in sys.stdin:
    op = mydict.get(line.strip(),"")
    if not op == "":
        print line.strip() + "=" + op
    else:
        print "Not found"
