def dfs(start):

    if len(stack) == m:
        print(' '.join(map(str,stack))) 
        return
    
    for i in range(start,n+1): 
        if not visited[i]: 
            visited[i] = True
            stack.append(i)
            dfs(i) #첫 번째 시작 숫자보다 낮은 숫자로 시작하는 것을 방지. 
            stack.pop()
            visited[i] = False

n, m = map(int,input().split())
visited = [False] * (n+1)
stack = []

dfs(1)