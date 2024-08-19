from collections import deque 
operation = []
stack = []

while(1):
    x = input()
    if x == '':
        operation.clear()
    if x == 'QUIT':
        break
    if x == 'END':
        n = int(input())
        for _ in range(n):
            stack.append(int(input()))

            for i in operation:

                if 'NUM' in i:
                    new = i.split(' ')
                    stack.append(int(new[1]))
                if i == 'DUP': #1번째 복제
                        stack.append(stack[0])
                        
                if i == 'POP': #1번쨰 팝
                        stack.pop()
                if i == 'INV': #1번째 부호변경
                        stack[0] = -stack[0]
                if i == 'SWP' and len(stack) >= 2: #1번째, 2번쨰 스왑
                        temp = stack[0]
                        stack[0] = stack[1]
                        stack[1] = temp
                if i == 'ADD' and len(stack) >= 2: #1번쨰, 2번쨰 합
                        stack[-2] = stack[-2] + stack[-1]
                        stack.pop()
                        
                if i == 'SUB' and len(stack) >= 2: #1번째, 2번쨰 차
                        stack[-2] = stack[-2] - stack[-1] 
                        stack.pop()
                if i == 'MUL' and len(stack) >= 2:
                        stack[-2] = stack[-2] * stack[-1]
                        stack.pop()
                        
                if i == 'DIV' and len(stack) >= 2:
                    if stack[-1] == 0:
                          print('error')
                          break
                    if stack[-2] < 0:
                            stack[-2] = (-stack[-2]) / stack[-1]
                            stack[-2] = -stack[-2]
                            stack.pop()
                    elif stack[-1] < 0:
                            stack[-2] = stack[-2] / (-stack[-1])
                            stack[-2] = -stack[-2]
                            stack.pop()
                    elif stack[-2] < 0 and stack[-1] <0:
                            stack[-2] = stack[-2] / stack[-1]
                            stack[-2] = -stack[-2]
                            stack.pop()
                    else:
                            stack[-2] = stack[-2] / stack[-1]
                            stack.pop()
                        
                if i == 'MOD' and len(stack) >= 2:
                    if stack[-1] == 0:
                          print('error')
                          break
                    if stack[-2] < 0:
                            stack[-2] = (-stack[-2]) % stack[-1]
                            stack[-2] = -stack[-2]
                            stack.pop()
                    elif stack[-1] < 0:
                            stack[-2] = stack[-2] % (-stack[-1])
                            stack[-2] = -stack[-2]
                            stack.pop()
                    elif stack[-2] < 0 and stack[-1] <0:
                            stack[-2] = stack[-2] % stack[-1]
                            stack[-2] = -stack[-2]
                            stack.pop()
                    else:
                            stack[-2] = stack[-2] % stack[-1]
                            stack.pop()   
            
            if len(stack) == 1:
                if stack[0] > 1000000000:
                      print('error')
                print(stack[0])
                
            else:
                print('error')   
            stack.clear()

        print()
    operation.append(x)

