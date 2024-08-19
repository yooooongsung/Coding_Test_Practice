N, K = map(int, input().split())
a = list(map(int, input().split()))
answer = 0
start, end = 0, 0
counter = [0] * (max(a) + 1)

while end < N:
    if counter[a[end]] < K:
        counter[a[end]] += 1
        end += 1
        answer = max(answer, end - start)  # 최대 길이 업데이트
    else:
        counter[a[start]] -= 1
        start += 1

print(answer)

