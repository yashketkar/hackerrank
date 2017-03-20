import math

def isPrime(n):
    if n<=1:
        return "Not prime"
    elif n<=3:
        return "Prime"
    elif n%2 == 0 or n%3 == 0:
        return "Not prime"
    else:
        for i in range(5,int(math.sqrt(n))+1,6):
            if n%i == 0 or n%(i+2) == 0:
                return "Not prime"
        return "Prime"

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    print isPrime(n)
