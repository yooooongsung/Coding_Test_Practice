#문자열 길이 차이 >> 할 수 있는 연산의 수
#S가 A일때, T에 AA가 없다면 1번 연산은 어차피 못함
#>> split을 활용해서, A끼리 뭉쳐있는 애들이 T에 있는지 확인
#>> 없다면 2번째 연산밖에 못함
s = input()
t = input()
round = len(t) - len(s)

def plusA(s,t):
    if s == t:
        return s
    if s.count('A') < t.count('A'): #T의 A 갯수가 더 많을 때
        x = s+'A'
        if x in t: #A를 뒤에 추가한 결과가 T에 존재한다면
            return plusA(x,t) #재귀돌리기
        else: #A를 추가한 결과가 T에 존재하지 않다면
            return reverseB(s,t)
    else:
        return reverseB(s,t)
    
def reverseB(s,t):
    if s == t:
        return s
    if s.count('B') < t.count('B'):
        x = s + 'B'
        if x[::-1] in t:
            return reverseB(x[::-1],t)
        else:
            return plusA(s,t)
    else:
        return plusA

if plusA(s,t) == reverseB(s,t):
    print(1)
else:
    print(0)


