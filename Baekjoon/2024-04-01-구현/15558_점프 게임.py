import sys
from collections import deque
input = sys.stdin.readline

n,k=map(int,input().split())
map_data=list()
map_data.append(input().rstrip())
map_data.append(input().rstrip())
visited=[[False for _ in range(n)] for _ in range(2)]
queue=deque()
time=-1
flag=False
queue.append([0,0])

visited[0][0]=True
while queue:
    for _ in range(len(queue)):
        y,x=queue.popleft()

        if x+1>=n or x+k>=n:
            flag=True
            break

        if map_data[y][x+1]=='1' and not visited[y][x+1]:
            queue.append([y,x+1])
            visited[y][x+1]=True

        if x-1>time+1 and map_data[y][x-1]=='1' and not visited[y][x-1]:
            queue.append([y,x-1])
            visited[y][x-1]=True

        if map_data[(y+1)%2][x+k]=='1' and not visited[(y+1)%2][x+k]:
            queue.append([(y+1)%2,x+k])
            visited[(y+1)%2][x+k]=True
    time+=1

print(1) if flag else print(0)