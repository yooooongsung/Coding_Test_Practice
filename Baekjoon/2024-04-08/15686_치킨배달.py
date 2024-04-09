import sys
n, m = map(int,sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

min_ans = sys.maxsize #2

chicken = []
home = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i,j])
        elif graph[i][j] == 1:
            home.append([i,j])

visit = [False] * (len(chicken)) #1


def dfs(idx,cnt):

    global min_ans

    if cnt == m:
        # print(visited[:])

        ans = 0

        for i in home: # 집 좌표에 대해 모든 치킨집과의 거리를 구함
            distance = sys.maxsize # 거리를 큰 수로 정의
            for j in range(len(visit)):
                if visit[j]:
                    check_num = abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
                    distance = min(distance,check_num) # 각 집에 대해 치킨 거리가 최소인 값을 구함
            ans +=distance
        min_ans = min(ans,min_ans)

        return

    for i in range(idx,len(chicken)):
        if not visit[i]:
            visit[i] = True
            dfs(i+1,cnt+1)
            visit[i]=False



dfs(0,0)

print(min_ans)