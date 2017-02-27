#!/usr/bin/python

import sys

# ---------------------------------------------------------------------------------
# Efficient function for finding combinations referenced from :
# http://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
import operator as op
def ncr(n, r):
    if n<r:
        return 0
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
# ---------------------------------------------------------------------------------

# DFS traversal of Adjacencey List
def dfs(start):
    currentlyVisited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in currentlyVisited:
            currentlyVisited.add(vertex)
            stack.extend(graph[vertex] - currentlyVisited)
    return currentlyVisited

# This is the graph representation in Adjacencey List form
graph = []
# This list marks 1 for visited and 0 for not visited during DFS traversal
visited = []
# This will be the list of lists containing the numbers which are together and cannot be paired up
together = []

# Enter your code here. Read input from STDIN. Print output to STDOUT
N,l = map(int,raw_input().split())

# Initialize graph and visited List
graph = [set() for _ in xrange(N)]
visited = [0 for _ in xrange(N)]

# Read and add the pairs in the graph
for i in range(l):
    a,b = map(int,raw_input().split())
    graph[a].add(b)
    graph[b].add(a)

# Perform DFS traversal to find links
for i in range(N):
    if visited[i]==0:
        visited[i] = 1
        currentlyVisited = dfs(i)
        together.append(list(currentlyVisited))
        for i in currentlyVisited:
            visited[i]=1

# These are the total number of unusable combinations
unusable = 0
for t in together:
    unusable = unusable + ncr(len(t),2)

# The total usable combinations
result = ncr(N,2) - unusable

# Compute the final result using the inputs from above
print result
