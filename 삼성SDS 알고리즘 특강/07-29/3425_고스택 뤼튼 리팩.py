from collections import deque 

def process_operation(stack, operation):
    for i in operation:
        if 'NUM' in i:
            new = i.split(' ')
            stack.append(int(new[1]))
        elif i == 'DUP':  # 1번째 복제
            if stack:
                stack.append(stack[-1])
        elif i == 'POP':  # 1번째 팝
            if stack:
                stack.pop()
        elif i == 'INV':  # 1번째 부호변경
            if stack:
                stack[0] = -stack[0]
        elif i == 'SWP' and len(stack) >= 2:  # 1번째, 2번째 스왑
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif i in ['ADD', 'SUB', 'MUL', 'DIV', 'MOD'] and len(stack) >= 2:
            a, b = stack[-2], stack[-1]
            if i == 'ADD':
                stack[-2] = a + b
            elif i == 'SUB':
                stack[-2] = a - b
            elif i == 'MUL':
                stack[-2] = a * b
            elif i == 'DIV':
                if b == 0:
                    print('ERROR')
                    return False
                stack[-2] = int(a / b) if a * b >= 0 else -(-a // b)
            elif i == 'MOD':
                if b == 0:
                    print('ERROR')
                    return False
                stack[-2] = a % b if a >= 0 else -(-a % b)
            stack.pop()
    return True

def main():
    operation = []
    
    while True:
        x = input()
        if x == '':
            operation.clear()
            continue
        if x == 'QUIT':
            break
        if x == 'END':
            n = int(input())
            for _ in range(n):
                stack = []
                stack.append(int(input()))
                
                if process_operation(stack, operation):
                    if len(stack) == 1:
                        if stack[0] > 1000000000:
                            print('ERROR')
                        else:
                            print(stack[0])
                    else:
                        print('ERROR')
            print()
            operation.clear()
        else:
            operation.append(x)

main()
# if __name__ == "__main__":
#     main()
