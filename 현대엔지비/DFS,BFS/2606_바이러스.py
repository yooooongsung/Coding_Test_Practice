import sys
from collections import deque, defaultdict #dict!!!
input = sys.stdin.readline
n = int(input())
m = int(input())
com = [] #defaultdict(list)

for _ in range(m):
    x,y = map(int,input().split())
    com.append([x,y])
    #com[x].append(y)
arr = []

def dfs(node):
    if node not in arr: #1,2,3 
        arr.append(node)
    for i in range(m):
        if com[i][0] == node and com[i][1] not in arr: #left -> right
            #print(str(node) + ' start to ' + str(com[i][1]))
            dfs(com[i][1])
        elif com[i][1] == node and com[i][0] not in arr: #right -> left
            #print(str(com[i][0]) + ' from ' + str(node)) 
            dfs(com[i][0])
    return

dfs(1)

print(len(arr)-1)

