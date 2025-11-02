def solution(n):
    answer = 1
    temp = 0
    start = 1
    add = 1
    while start != n:
        if temp == n:
            answer += 1
            start += 1
            temp = 0
            add = start
        if temp > n:
            start += 1
            temp = 0
            add = start
        else:
            temp += add
            add += 1
        
        
    return answer