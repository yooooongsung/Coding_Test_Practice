from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    zone_id = 1
    zone = dict()
    
    def bfs(x, y, cnt):
        q = deque()
        q.append((x, y))
        
        visited[x][y] = True
        land[x][y] = zone_id
        
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        land[nx][ny] = zone_id
                        cnt += 1
                        
        return cnt
    for i in range(m):
        for j in range(n):
            if land[j][i] == 1 and not visited[j][i]:
                res = bfs(j, i, 1)
                zone[zone_id] = res
                zone_id += 1
                
    used_id = []
    answer = []
    for i in range(m):
        result = 0
        for j in range(n):
            if land[j][i] != 0 and land[j][i] not in used_id:
                used_id.append(land[j][i])
        for zid in used_id:
            result += zone[zid]
                
        answer.append(result)
        used_id.clear()
            
    return max(answer)  # 아직 answer 안 만들었으니 그냥 0 반환