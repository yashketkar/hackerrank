#!/bin/python
try:
    print int(raw_input().strip())
except ValueError:
    print "Bad String"
