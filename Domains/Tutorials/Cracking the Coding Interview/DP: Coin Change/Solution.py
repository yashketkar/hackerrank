#!/bin/python
import sys
memo = {}
def my_make_change(coins, money, index):
	if str(money)+"_"+str(index) in memo.keys():
		return memo[str(money)+"_"+str(index)]
	if money==0:
		return 1
	if index >= len(coins):
		return 0
	amountWithCoin = 0
	ways = 0
	while(amountWithCoin <= money):
		remaining = money - amountWithCoin
		ways += my_make_change(coins,remaining,index+1)
		amountWithCoin += coins[index]
	memo[str(money)+"_"+str(index)] = ways
	return ways
def make_change(coins, n):
	myways = my_make_change(coins, n, 0)
	return myways
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)
