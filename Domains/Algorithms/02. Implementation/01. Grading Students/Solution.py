#!/bin/python
def round(g):
    if g >= 38 and (g - g%5 + 5) - g < 3:
        return g - g%5 + 5
    else:
        return g
n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    print round(grade)
