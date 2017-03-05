#!/bin/python3

import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
k = k%n
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a2 = a[n-k:n] + a[:n-k]
for a0 in range(q):
    m = int(input().strip())
    print(a2[m])