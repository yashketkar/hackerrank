#!/bin/python3

import sys

def score(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return 0

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice = score(a0,b0)+score(a1,b1)+score(a2,b2)
bob = score(b0,a0)+score(b1,a1)+score(b2,a2)

print(alice, bob)