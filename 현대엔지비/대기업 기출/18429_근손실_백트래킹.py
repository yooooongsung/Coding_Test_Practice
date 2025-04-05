import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kits = list(map(int, input().split()))
visited = [False] * n
cnt = 0  # 가능한 경우의 수

def dfs(day, weight):
    global cnt
    if day == n:
        cnt += 1
        return
    
    for i in range(n):
        if not visited[i]:
            new_weight = weight + kits[i] - k
            if new_weight >= 500:
                visited[i] = True
                dfs(day+1, new_weight)
                visited[i] = False

dfs(0,500)
print(cnt)