def dfs(row, column):
    if row < 0 or row >= n or column < 0 or column >= n: #for문에서 온 행렬 값이 인덱스 범위 밖을 넘는지 확인
        return 0
    if visited[row][column] or arr[row][column] == 0: #이미 방문했거나, 집이 없는 경우 확인
        return 0

    visited[row][column] = True #현재 집 방문 처리
    cnt = 1  # 현재 집 포함
    # 상하좌우 탐색
    cnt += dfs(row + 1, column) #dfs가 불릴 때마다 위 조건에서 확인 후 방문처리 및 cnt = 1로 반환.
    cnt += dfs(row - 1, column)
    cnt += dfs(row, column + 1)
    cnt += dfs(row, column - 1)
    return cnt 

n = int(input()) #격자 행렬 길이
visited = [[False for _ in range(n)] for _ in range(n)] #2차원 방문 체크 리스트
arr = [list(map(int, input())) for _ in range(n)] #격자

towns = []  # 각 단지별 집의 개수 저장

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]: #처음부터 방문할 집들만 가려냄 : 격자에서 1이 있고, 방문하지 않은 집
            towns.append(dfs(i, j)) #그리고 그 방문하지 않은 좌표를 dfs() 함수로 돌림 -> dfs함수에서 나온 값은 각 단지내의 집들의 숫자임

print(len(towns))  # 단지 개수 출력
for town in sorted(towns):
    print(town)  # 각 단지별 집의 개수 오름차순으로 출력

"""
def dfs(row, column,cnt):
    for i in range(row,n):
        for j in range(column,n):
            if not visited[i][j] and arr[i][j] == 1:

                visited[i][j] = True
                cnt += 1
                
                if j < n-1 and arr[i][j+1] == 1 and not visited[i][j+1]: #오른쪽에 1이 있을때
                    dfs(i,j+1,cnt)
                elif i < n-1 and arr[i+1][j] == 1 and not visited[i+1][j]: #아래에 1이 있을때
                    dfs(i+1,j,cnt)
                elif j > 0 and arr[i][j-1] == 1 and not visited[i][j-1]:
                    dfs(i,j-1,cnt)
                elif i > 0 and arr[i-1][j] == 1 and not visited[i-1][j]:
                    dfs(i-1,j,cnt)
                else:
                    print(cnt)
                    return
            else:
                continue
        
    return

column = 0
row = 0
town = 0
cnt = 0
n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]

arr = [list(map(int,input())) for _ in range(n)]
dfs(row,column,cnt)
"""