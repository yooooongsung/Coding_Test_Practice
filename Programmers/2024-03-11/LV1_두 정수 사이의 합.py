def solution(a, b):
    answer = 0
    arr = []
    if a < b:
        while a < b:
            arr.append(a)
            a+=1
        arr.append(b)
        answer = sum(arr)
    elif a > b:
        while a > b:
            arr.append(b)
            b+=1
        arr.append(a)
        answer = sum(arr)
    else:
        answer = a
    
    
    return answer

print(solution(3,10))