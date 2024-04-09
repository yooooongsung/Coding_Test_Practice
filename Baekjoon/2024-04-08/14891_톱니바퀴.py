wheels = [[int(i) for i in input()] for _ in range(4)]

k = int(input())

turns = [list(map(int,input().split())) for _ in range(k)]

for i in range(k):
    if i != 1 and i != 4 and turns[i][1] == -1: #시계방향으로 돌릴 경우에 비교 대상은 그 다음 톱니바퀴임. 
        #고로 4번 톱니바퀴는 시계방향으로 돌렸을 때 영향을 주는 톱니바퀴가 그 전의 톱니바퀴임
        if wheels[i][2] != wheels[i+1][6]: #오른쪽 톱니와 다를때
            temp = wheels[i][0]
            del wheels[i][0]
            wheels[i].append(temp)
        if wheels[i][2] == wheels[i+1][6]: #오른쪽 톱니와 같을 때

        if wheels[i][6] != wheels[i-1][2]: #왼쪽 톱니와 다를 때

        if wheels[i][6] == wheels[i-1][2]: #왼쪽 톱니와 같을 때
        

