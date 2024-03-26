def dfs(ax,ay,bx,by):
    visited[ax,ay] = True
    visited[bx,by] = True

    num = 0
    for i in range(4):
        nax = dx[i] + ax
        nay = dy[i] + ay
        if not visited[nax][nay] and matrix[nax][nay] > num:#A가 상하좌우 돌고 가장 큰 값을 num에 저장함
            num = matrix[nax][nay] 
            max_ax = nax #max 값의 인덱스를 담음
            max_ay = nay

    if not visited[max_ax][max_ay]: #방문하지 않았다면 
        dfs(max_ax,max_ay) #dfs(max 좌표 전달)

    for i in range(4):
        nbx = dx[i] + bx
        nby = dy[i] + by
        if matrix[nbx][nby] > num:#b가 상하좌우 돌고 가장 큰 값을 num에 저장함
            num = matrix[nbx][nby]
            max_bx = nbx
            max_by = nby
        
    

    

    for _ in range(3): #3초 동안 돌거임
                        #A가 먼저 상하좌우를 탐색하며 가장 큰 값을 차지, visited = True
                        #그 다음 B가 상하좌우 탐색하며 가장 큰 값 차지, visited = True
    return


n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
ax,ay= map(int,input().split())
bx,by = map(int,input().split())
visited = [[False] * n for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

dfs(ax-1,ay-1,bx-1,by-1) #행렬 값 -1 -> 매트릭스에 맞게 인덱스 조정
