import sys
first = list(map(int,sys.stdin.readline().split()))
second = list(map(int,sys.stdin.readline().split()))

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)
    

def add(first, second):
    child = first[0] * second[1] + first[1] * second[0]
    parent = first[1] * second[1]
    x = gcd(child, parent) 
    child //= x
    parent //= x
    print(child, parent)

add(first,second)


