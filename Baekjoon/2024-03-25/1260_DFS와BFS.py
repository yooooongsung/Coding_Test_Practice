def dfs(v):
    
    visited[v] = True
    print(v, end=' ')  # 방문한 정점 출력
    for i in graph[v]:
        if not visited[i]: #방문하지 않은 i에 대해서만 dfs 재귀 돌리기
            dfs(i)
    
    
          
    

def bfs(v):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            bfs(i)
        
        



n,m,v = map(int,input().split()) # 정점의 갯수 : n, 간선의 갯수 : m, 시작정점 번호 : v
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


dfs(v)
bfs(v)


