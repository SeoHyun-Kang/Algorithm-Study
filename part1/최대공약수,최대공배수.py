a, b = map(int,input().split())

def gcd(x,y):
    while y!=0:
        mod = x%y
        x = y
        y = mod
    return x

def lcm(x,y):
    m = (x*y) / gcd(x,y)
    return m

print(gcd(a,b))
print(lcm(a,b))

'''
import math
a,b = map(int,input().split())
print(math.gcd(a,b))
print(math.lcm(a,b))
'''