import sys
t = int(input())

def com(n,r):
    result = 1
    if r == 0 or n == r:
        return 1
    for _ in range(r):
        result *= n
        n -= 1
    
    div = 1
    for i in range(r,0,-1):
        div *= i
    
    return result // div

for _ in range(t):
    n , m = map(int,sys.stdin.readline().split())
    print(com(m,n))

