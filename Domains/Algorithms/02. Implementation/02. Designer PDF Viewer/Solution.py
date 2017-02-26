#!/bin/python3

import sys

h = list(map(int, input().strip().split(' ')))
wordlist = list(input().strip())
abc = list('abcdefghijklmnopqrstuvwxyz')
height = 0
for i in wordlist:
    j = abc.index(i)
    if height < h[j]:
        height = h[j]
area = height*len(wordlist)
print(area)