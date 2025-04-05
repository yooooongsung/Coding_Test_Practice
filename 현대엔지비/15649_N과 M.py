import sys
input = sys.stdin.readline
n,m = map(int,input().split())

def p():
    for i in range(len(arr)):
        print(i)

def dfs(n,m):
    if len(arr) == m:
        print(arr)
        arr = []
    
dfs(n,m)