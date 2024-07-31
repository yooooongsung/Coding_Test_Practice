import sys
arr = list(sys.stdin.readline())
stack = []
result = 1
answer = 0
for i in range(len(arr)):
    if arr[i] == '(':
        result *= 2
        stack.append(arr[i])
    elif arr[i] == '[':
        result *= 3
        stack.append(arr[i])
    elif arr[i] == ')':
        if not stack or stack[-1] == '[':  #stack[-1] 과 arr[i-1]은 같은가?
            answer = 0
            break
        else: #여기서 else를 쓰면 안되는 이유?
            if arr[i-1] == '(':
                answer += result
            stack.pop()
            result //= 2
                
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        else:
            if arr[i-1] == '[':
                answer += result
            stack.pop()
            result //= 3
if stack:
    print(0)
else:
    print(answer)
    
    
#1. 무조건 여는 괄호가 있어야 곱하건 뺴건 가능하다.
# 그러므로 result = 1로 초기화하는 것은 전혀 문제가 없다

#2. stack에 들어가는 요소는 여는 괄호만 들어간다. 
# 닫는 괄호가 나오면, 여는 괄호를 pop시켜 stack을 비우고 연산을 마친다.