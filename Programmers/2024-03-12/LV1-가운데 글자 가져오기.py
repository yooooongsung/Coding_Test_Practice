def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        a = len(s) // 2
        answer = s[a-1:a+1]
    else:
        a = len(s) // 2
        answer = s[a]
    
    return answer

print(solution("abcde")) #"c"
print(solution("qwer")) #"we"

#https://school.programmers.co.kr/learn/courses/30/lessons/12903