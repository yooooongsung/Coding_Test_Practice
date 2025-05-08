from collections import deque
def bfs(x,y,n):
    q = deque()
    visited = set()
    dx = [2,3]
    
    q.append((x,0))
    visited.add(x)
    
    while q:
        a, cnt = q.popleft() #(10,0) / (15,1), (20,1), (30,1) / 
        if a == y:
            return cnt
        for i in range(3):
            if  i == 0:
                nx = a + n
            else:
                nx = a * dx[i-1]
            
            if nx <= y  and nx not in visited:
                q.append((nx,cnt+1))
                visited.add(nx)
    return -1
            
def solution(x, y, n):
    return bfs(x,y,n)