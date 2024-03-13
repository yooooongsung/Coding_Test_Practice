def solution(phone_number):
    answer = ''
    length = len(phone_number) - 4
    rear = phone_number[-4:]
    answer = '*'* length + rear
    return answer

print(solution("01034678006")) #*******8006
print(solution("1224")) #1224

#https://school.programmers.co.kr/learn/courses/30/lessons/12948