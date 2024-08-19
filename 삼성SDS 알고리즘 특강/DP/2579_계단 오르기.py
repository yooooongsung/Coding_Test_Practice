#1계단 혹은 점프 가능
#근데 3계단 연속은 불가능
#이건 탑다운 방식일듯! max값 찾기 // 바텀업도 가능하다
#각 상황마다 두가지 선택지가 있음
#바닥에서 첫번째를 선택하기, 혹은 점프하기
#무조건 첫번째를 밟아야한다? 초기값일듯
import sys
n = int(sys.stdin.readline())
score = []
for _ in range(n):
    x = int(sys.stdin.readline())
    score.append(x)
dp = [0] * n #[0,0,0,0,0,0]
dp[0] = score[0] #초기값 설정
cnt = 0
for i in range(2,n):
    if score[i] > score[i-1]:
        dp[i] = score[i]
    else:
        dp[i-1] = score[i-1]
        cnt += 1
        i += 1
        if cnt == 3:
            dp[i-1] = 0
            cnt = 0
            i -= 1

print(sum(dp))
    