import sys
n, k = map(int,sys.stdin.readline().split())
def fac(x, result):
    if x == 0:
        return 1
    if x == 1:
        return result
    else:
        result *= x
        return fac(x-1,result)
        
a = fac(n,1)
b = fac(n-k,1)
c = fac(k,1)

print((a // (b*c)))
