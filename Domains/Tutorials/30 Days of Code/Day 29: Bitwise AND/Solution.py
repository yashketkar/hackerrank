#!/bin/python
import sys
def findMaxAnd(n,k):
    maxAnd = 0
    for i in range(1,n):
        if k&i > maxAnd and k!=i and k&i <= k:
            maxAnd = k&i
    return maxAnd
t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    print findMaxAnd(n+1,k-1)
