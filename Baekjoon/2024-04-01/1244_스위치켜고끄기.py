#남자애는 스위치 번호의 배수를 끄거나 킨다
#여자애는 받은 스위치 번호 기준으로 양쪽이 둘 다 켜져있거나 꺼져있으면 
#확장검사하며 구간 모두의 상태를 바꾼다

n = int(input())
switch = list(map(int,input().split()))
students = int(input())
sex_num = [list(map(int,input().split())) for _ in range(students)]

for i in range(len(sex_num)):
    if sex_num[i][0] == 1: #남학생이라면
        for j in range(1,n+1):
            if j % sex_num[i][1] == 0: #스위치 번호가 남학생 배정 스위치의 배수일 때
                switch[j-1] = not switch[j-1] #스위치를 바꿈
    else: #여학생이라면
        girl = sex_num[i][1] - 1 #우선 본인 위치 스위치 인덱스를 담음
        switch[girl] = not switch[girl] #그리고 스위치 상태 바꿈
        if switch[girl-1] == switch[girl + 1]: #만약 좌우의 스위치 상태가 같다면
            switch[girl-1] = not switch[girl-1] #바꿈
            switch[girl + 1] = not switch[girl + 1] #바꿈
            