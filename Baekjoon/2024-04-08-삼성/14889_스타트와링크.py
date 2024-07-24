import sys
n = int(sys.stdin.readline())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
visit = [ False for _ in range(n) ] #1
min_value = sys.maxsize #2

def backTracking(depth, idx): #3
    global min_value
    if depth == n // 2: #4
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]: #5
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]: #6
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1-power2)) #7
        return

    for i in range(idx, n): #8
        if not visit[i]:
            visit[i] = True
            backTracking(depth+1, i+1) #9
            visit[i] = False
backTracking(0, 0)
print(min_value)