import sys

<<<<<<< HEAD
while(1):
    x = input()
    if x == '':
        operation.clear()
    if x == 'QUIT':
        break
    if x == 'END':
=======
input = sys.stdin.readline
def process_operation(operations, first):
        stack = [first]
        for operation in operations:
                if 'NUM' in operation:
                        new = operation.split(' ')
                        stack.append(int(new[1]))
                elif not stack:
                        return "ERROR"
                elif operation == 'DUP':
                        stack.append(stack[-1])
                elif operation == 'POP':
                        stack.pop()
                elif operation == 'INV':
                        stack[-1] *= -1
                elif len(stack) == 1:
                        return 'ERROR'    
                elif operation == 'ADD':
                        temp = stack.pop() + stack.pop()
                        if abs(temp) > 10 ** 9:
                                return 'ERROR'
                        stack.append(temp)
                elif operation == 'SWP':
                        stack[-1], stack[-2] = stack[-2], stack[-1]   
                elif operation == 'SUB':
                        temp = -stack.pop() + stack.pop()
                        if abs(temp) > 10 ** 9:
                                return 'ERROR'
                        stack.append(temp)                
                elif operation == 'MUL':
                        temp = stack.pop() * stack.pop()
                        if abs(temp) > 10 ** 9:
                                return 'ERROR'
                        stack.append(temp)
                elif operation == 'DIV':
                        a , b = stack.pop(), stack.pop()
                        if a == 0:
                                return 'ERROR'
                        temp = abs(b) // abs(a)
                        if (a > 0 and b < 0) != (a < 0 and b > 0):  # 피연산자 중 하나가 음수일 경우
                                temp = -temp
                        if abs(temp) > 10 ** 9:
                                return 'ERROR'
                        stack.append(temp)
                                
                elif operation == 'MOD':# 나머지 계산
                        a , b = stack.pop(), stack.pop()
                        if a == 0:
                                return 'ERROR'
                        temp = abs(b) % abs(a)
                        if a < 0:
                                temp = -temp
                        if abs(temp) > 10 ** 9:
                                return 'ERROR'
                        stack.append(temp)
                else:
                        return "ERROR"

        if len(stack) == 1:
            return stack[0]
        return 'ERROR'



    
while True:
        operations = []
        while True:
                operation = input().strip()
                if operation == "QUIT":
                        quit()
                if operation == "END":
                        break
                operations.append(operation)
        
>>>>>>> 4e25f45a9610c04149988d93fe7d1b7281bb86c5
        n = int(input())
        for _ in range(n):
                first = int(input())
                print(process_operation(operations,first))
                
        print()
        input()
                
# import sys

# input = sys.stdin.readline

<<<<<<< HEAD
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

=======
# def exec(commands, num):
#     stack = [num]
#     for cmd in commands:
#         if cmd[:3] == "NUM":
#             n = int(cmd[4:])
#             stack.append(n)
#         elif not stack:
#             return "ERROR"
#         elif cmd == "POP":
#             stack.pop()
#         elif cmd == "INV":
#             stack[-1] *= -1
#         elif cmd == "DUP":
#             stack.append(stack[-1])
#         elif len(stack) == 1:
#             return "ERROR"
#         elif cmd == "SWP":
#             stack[-1], stack[-2] = stack[-2], stack[-1]
#         elif cmd == "ADD":
#             temp = stack.pop() + stack.pop()
#             if abs(temp) > 10 ** 9:
#                 return "ERROR"
#             stack.append(temp)
#         elif cmd == "SUB":
#             temp = -stack.pop() + stack.pop()
#             if abs(temp) > 10 ** 9:
#                 return "ERROR"
#             stack.append(temp)
#         elif cmd == "MUL":
#             temp = stack.pop() * stack.pop()
#             if abs(temp) > 10 ** 9:
#                 return "ERROR"
#             stack.append(temp)
#         elif cmd == "DIV":
#             a, b = stack.pop(), stack.pop()
#             if a == 0:
#                 return "ERROR"
#             temp = abs(b) // abs(a)
#             if (a > 0 and b < 0) or (a < 0 and b > 0):
#                 temp = -temp
#             if abs(temp) > 10 ** 9:
#                 return "ERROR"
#             stack.append(temp)
#         elif cmd == "MOD":
#             a, b = stack.pop(), stack.pop()
#             if a == 0:
#                 return "ERROR"
#             temp = abs(b) % abs(a)
#             if b < 0:
#                 temp = -temp
#             if abs(temp) > 10 ** 9:
#                 return "ERROR"
#             stack.append(temp)
#         else:
#             return "ERROR"

#     if len(stack) == 1:
#         return stack[0]
#     return 'ERROR'


# while True:
#     commands = []
#     while True:
#         cmd = input().strip()
#         if cmd == "QUIT":
#             quit()
#         if cmd == "END":
#             break
#         commands.append(cmd)

#     n = int(input())
#     for _ in range(n):
#         num = int(input())
#         print(exec(commands, num))
#     print()
#     input()  # 줄바꿈 삭제
>>>>>>> 4e25f45a9610c04149988d93fe7d1b7281bb86c5
