def solution(s):
    answer = True
    a = s.count('p')
    b = s.count('P')
    c = s.count('y')
    d = s.count('Y')
    if a+b == c+d:
        answer = True
    else:
        answer = False

    # 보완코드
    # s = s.lower() 
    # if s.count('p) == s.count(y):
        # return True
    # return False

    return answer

print(solution('pypypsdpqyz'))

#https://school.programmers.co.kr/learn/courses/30/lessons/12916