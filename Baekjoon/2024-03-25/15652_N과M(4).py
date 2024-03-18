def dfs(start): #start 파라미터 
    
    
    if len(stack) == m:

        print(' '.join(map(str,stack)))
        return
    
    for i in range(start,n+1):
        
        stack.append(i)
        dfs(i) #stack에 푸시되는 같은 값을 재귀함수 아규먼트로 
        stack.pop()

n,m = map(int,input().split())
stack = []
dfs(1)

