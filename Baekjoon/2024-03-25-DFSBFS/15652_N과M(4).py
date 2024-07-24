def dfs(start): #start 파라미터 
    
    
    if len(stack) == m:

        print(' '.join(map(str,stack)))
        return
    
    for i in range(start,n+1):
        
        stack.append(i)
        dfs(i) #stack에 푸시되는 같은 값을 재귀함수 아규먼트로 -> i의 값이 바뀔 때 같이 바뀌기 때문에 크거나 같은 값으로 스택에 푸시 가능
        stack.pop()

n,m = map(int,input().split())
stack = []
dfs(1)

