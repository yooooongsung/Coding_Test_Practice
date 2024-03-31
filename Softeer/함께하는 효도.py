def dfs(ax,ay,bx,by):

    global answer
    answer = matrix[ax][ay] + matrix[bx][by]
    cnt = 0
    
    if cnt == 3:
        print(answer)
    
    max_a = 0
    max_b = 0
    
    for i in range(4):
        nax = dx[i] + ax
        nay = dy[i] + ay
        if 0 <= nax < n and 0 <= nay < n:
            if not visited[nax][nay] and matrix[nax][nay] > max_a:#A가 상하좌우 돌고 가장 큰 값을 max_a에 저장함
                max_a = matrix[nax][nay] 
                max_ax = nax #max 값의 인덱스를 담음
                max_ay = nay

    visited[max_ax][max_ay] = True
        

    for i in range(4):
        nbx = dx[i] + bx
        nby = dy[i] + by
        if 0 <= nbx < n and 0 <= nby < n:
            if not visited[nbx][nby] and matrix[nbx][nby] > max_b:#b가 상하좌우 돌고 가장 큰 값을 max_b에 저장함
                max_b = matrix[nbx][nby]
                max_bx = nbx
                max_by = nby

    visited[max_bx][max_by] = True
    
    cnt = cnt + 1
    dfs(max_ax,max_ay,max_bx,max_by)
    

    

    


n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
ax,ay= map(int,input().split())
bx,by = map(int,input().split())
visited = [[False] * n for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited[ax-1][ay-1] = True
visited[bx-1][by-1] = True
dfs(ax-1,ay-1,bx-1,by-1) #행렬 값 -1 -> 매트릭스에 맞게 인덱스 조정
