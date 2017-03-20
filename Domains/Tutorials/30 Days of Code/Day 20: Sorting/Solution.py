#!/bin/python
import sys
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
swaps = 0
for i in range(len(a)):
    s = 0
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
            swaps = swaps + 1
            s = s+1
    if s == 0:
        break
print "Array is sorted in " + str(swaps) +" swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])
