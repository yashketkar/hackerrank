#!/bin/python
import sys
import re
N = int(raw_input().strip())
fname = []
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.match(".*?@gmail.com",emailID) !=None:
        fname.append(firstName)
for i in sorted(fname):
    print i
