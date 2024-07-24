#남자애는 스위치 번호의 배수를 끄거나 킨다
#여자애는 받은 스위치 번호 기준으로 양쪽이 둘 다 켜져있거나 꺼져있으면 
#확장검사하며 구간 모두의 상태를 바꾼다

n = int(input())
switch = list(map(int,input().split()))
students = int(input())
sex_num = [list(map(int,input().split())) for _ in range(students)]

def girl(x,sex_num):
    
    if sex_num - x >= 0 and sex_num + x < n and switch[sex_num - x] == switch[sex_num + x]: #만약 좌우의 스위치 상태가 같다면
        
        if switch[sex_num - x] == 1: #바꿈
            switch[sex_num - x] = 0
        else:
            switch[sex_num - x] = 1
        if switch[sex_num + x] == 1:
            switch[sex_num + x] = 0
        else:
            switch[sex_num + x] = 1
        girl(x+1,sex_num)
    else:
        return

for i in range(len(sex_num)):
    if sex_num[i][0] == 1: #남학생이라면
        for j in range(1,n+1):
            if j % sex_num[i][1] == 0: #스위치 번호가 남학생 배정 스위치의 배수일 때
                if switch[j-1] == 1:
                    switch[j-1] = 0
                else:
                    switch[j-1] = 1 #스위치를 바꿈
    else: #여학생이라면
        if switch[sex_num[i][1]-1] == 1:#본인꺼 스위치 상태 바꿈
            switch[sex_num[i][1]-1] = 0
        else:
            switch[sex_num[i][1]-1] = 1 
        girl(1,sex_num[i][1]-1) #1과 현재위치를 넘겨줌

for i in range(len(switch)):
    # 원소 출력
    print(switch[i], end=' ')
    # i가 0부터 시작하므로, i+1로 조건을 맞추고, 20의 배수가 될 때마다 새로운 줄로 넘어감
    if (i + 1) % 20 == 0:
        print()  # 새로운 줄로 넘어가기
            