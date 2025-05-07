def solution(order):
    answer = 0
    sub_stack = []
    #기본 컨베는 큐
    #보조 컨베는 스택
    j = 0
    for i in range(len(order)):
        if order[j] == i+1:
            answer += 1
            j += 1
        else:
            sub_stack.append(i+1)
        while True:
            if sub_stack and sub_stack[-1] == order[j]:
                sub_stack.pop()
                answer += 1
                j += 1
            else:
                break
                
    return answer