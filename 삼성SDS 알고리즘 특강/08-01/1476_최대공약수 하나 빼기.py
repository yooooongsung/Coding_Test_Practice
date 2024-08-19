import sys
from collections import deque
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
q = deque(arr)
save = []

def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)
    
    
for i in range(n):
    save.append(q.popleft())
    cur = gcd(q[i],q[i+1])
    
    
