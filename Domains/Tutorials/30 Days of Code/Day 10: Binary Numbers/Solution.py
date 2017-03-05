#!/bin/python
n = int(raw_input().strip())
i=0
while n!=0:
    n = n & (n<<1)
    i = i+1
print i
