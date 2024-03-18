def dfs(start): #start 파라미터 
    
    
    if len(stack) == m:

        print(' '.join(map(str,stack)))
        return
    
    
    for i in range(start,n+1):
        if visited[i]: 
            continue
        visited[i] = True  
        stack.append(i) 
        dfs(i+1) #아규먼트로 그 다음값부터 시작하도록함
        stack.pop()
        visited[i] = False    
        
    

n,m = map(int,input().split())
stack = []
visited = [False] * (n+1)
dfs(1)

