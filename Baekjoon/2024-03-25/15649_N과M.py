def dfs():
    
    
    if len(stack) == m:
        print(' '.join(map(str,stack)))
        return
    
    
    for i in range(1,n+1):
        if visited[i]: #i가 visited에 있다면 다음 인덱스로 
            continue
        visited[i] = True #1부터 visited를 True로 
        stack.append(i) #스택에 1부터 쌓음
        dfs() #이미 visited[1]은 True이다. 그래서 continue -> 2부터 시작
        stack.pop()
        visited[i] = False    
        
    

n,m = map(int,input().split())
stack = []
visited = [False] * (n+1)
cnt = 0
dfs()
