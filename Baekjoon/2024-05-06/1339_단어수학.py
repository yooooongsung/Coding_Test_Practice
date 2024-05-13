n = int(input())
alphabet = []
visited = ['A','B','C','D','E','F','G','H','I','J']
for _ in range(n):
    i = input()
    alphabet.append(i)
maxi = ''
for i in range(n):
    if len(alphabet[i]) > len(maxi):
        maxi = alphabet[i]
        max_index = alphabet.index(maxi)

#1) maxi에 나오는 알파벳에 숫자 부여, 
#2) 남은 알파벳 배열 중에서 해당 알파벳을 가지고 있는 지 체크
#3) 가지고 있다면 해당 숫자를 부여
#4) 가지고 있지 않다면 maxi에게 숫자를 다 부여하고
#5) 나머지 배열의 문자열들에게도 순차적으로 숫자를 부여
start_num = '9'
for i in range(len(maxi)):
    if maxi[i] in visited:
        maxi[i] = start_num - 1
        if 

