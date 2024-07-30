def process_operation(stack, operations):
    for operation in operations:
        if 'NUM' in operation:
            _, num = operation.split()
            stack.append(int(num))
        elif not stack:
            return "ERROR"
        elif operation == 'DUP':
            stack.append(stack[-1])
        elif operation == 'POP':
            stack.pop()
        elif operation == 'INV':
            stack[-1] = -stack[-1]
        elif operation == 'SWP':
            if len(stack) < 2:
                return False
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif operation in ['ADD', 'SUB', 'MUL', 'DIV', 'MOD']:
            if len(stack) < 2:
                return False
            b = stack.pop()
            a = stack.pop()
            if operation == 'ADD':
                stack.append(a + b)
            elif operation == 'SUB':
                stack.append(a - b)
            elif operation == 'MUL':
                stack.append(a * b)
            elif operation == 'DIV':
                if b == 0:
                    return 'ERROR'
                # 나눗셈의 절댓값을 사용하여 계산
                a_abs, b_abs = abs(a), abs(b)
                result = a_abs // b_abs
                if (a < 0) != (b < 0):  # 피연산자 중 하나가 음수일 경우
                    result = -result
                stack.append(result)
            elif operation == 'MOD':
                if b == 0:
                    return 'ERROR'
                # 나머지 계산
                result = a % b
                if a < 0:
                    if b < 0:
                        result = -(-a % -b)
                    else:
                        result = -(-a % b)
                    print('11')
                elif a > 0:
                    if b < 0:
                        result = a % -b
                    else:
                        result = a % -b
                    print('22')
                stack.append(result)

    return True

def main():
    operations = []
    
    while True:
        x = input()
        if x == '':
            operations.clear()
            continue
        if x == 'QUIT':
            break
        if x == 'END':
            n = int(input())
            results = []
            for _ in range(n):
                stack = []
                stack.append(int(input()))
                
                if process_operation(stack, operations):
                    if len(stack) == 1:
                        if stack[0] > 1000000000:
                            results.append('ERROR')
                        else:
                            results.append(str(stack[0]))
                    else:
                        results.append('ERROR')
                else:
                    results.append('ERROR')
            print("\n".join(results))
            print()
            operations.clear()
        else:
            operations.append(x)

if __name__ == "__main__":
    main()