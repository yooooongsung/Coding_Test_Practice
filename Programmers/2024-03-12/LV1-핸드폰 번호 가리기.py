def solution(phone_number):
    answer = ''
    rear = phone_number[-1:-5:-1]
    length = len(phone_number) - 4
    for i in range(length):
        answer = answer + '*'
    return answer + rear