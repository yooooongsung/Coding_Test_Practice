import sys
n, m = map(int,input().split())
dict = {}
for _ in range(m):
    num, a, b = sys.stdin.readline().split()
    if num == '0': #합치기
        if a in dict: #key값이 딕셔너리에 있다면
            dict[a].append(b) #배열로 value값을 넣어줌
        else:
            dict[a] = [b] #key값이 딕셔너리에 없다면, 새로 추가
    elif num == '1':
        check = dict.get(a) #get함수로 key 값으로 value에 접근 >> check에 저장
        if b in check: #b 값이 check에 있다면
            print('YES') 
        else: #없다면
            print('NO')