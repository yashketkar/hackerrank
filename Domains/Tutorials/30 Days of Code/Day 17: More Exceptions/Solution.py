import math
#Write your code here
class Calculator:
    def __init__(self):
        self = self
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        else:
            return int(math.pow(n,p))
