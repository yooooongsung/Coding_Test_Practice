def dfs():
    if len(stack) == m:
        print(' '.join(map(str,stack)))
        return #스택의 길이가 m개가 되는 순간 돌아감

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            stack.append(i) #
            dfs()
            stack.pop()
            visited[i] = False
            


n, m = map(int,input().split())
visited = [False] * (n+1)
stack = []
dfs()
