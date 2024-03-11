def solution(n):
    answer = []
    num = str(n)
    for i in range(-1,-(len(num)+1),-1):
        answer.append(int(num[i]))
        
    return answer

    #option2. 정수형 변환 후 answer.append() -> 반복문 탈출 후 answer.reverse

print(solution(123423145)) 

#https://school.programmers.co.kr/learn/courses/30/lessons/12932