from collections import deque
def dfs(v):
    
    visited1[v] = True
    print(v, end=' ')  # 방문한 정점 출력
    for i in graph[v]:
        if not visited1[i]: #방문하지 않은 i에 대해서만 dfs 재귀 돌리기
            dfs(i)
    
    
          
    

def bfs(v):
    
    deq = deque([v]) #데크에 노드를 넣음
    visited2[v] = True 
    while deq: #데크에 원소가 없을 때까지 반복

        head = deq.popleft() #데크의 왼쪽 원소를 팝
        print(head,end=' ') #왼쪽 원소부터 순서대로 출력

        for i in graph[head]: #head와 인접한 모든 노드를 체크
            if not visited2[i]: #만약 방문하지 않은 노드라면
                visited2[i] = True #방문 완료 표시하고
                deq.append(i) #데크에 추가
            
        



n,m,v = map(int,input().split()) # 정점의 갯수 : n, 간선의 갯수 : m, 시작정점 번호 : v
graph = [[] for _ in range(n + 1)]

visited1 = [False] * (n + 1) 
visited2 = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


dfs(v)
print()
bfs(v)


