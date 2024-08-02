import sys
import itertools

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

if m[0] == 1:  # 1번 문제의 경우
    k = m[1] - 1  # 0-indexed로 변환
    arr = list(range(1, n + 1))
    
    # k번째 순열 찾기
    result = []
    while n > 0:
        f = factorial(n - 1)
        idx = k // f
        result.append(arr[idx])
        arr.pop(idx)
        k %= f
        n -= 1
    
    print(' '.join(map(str, result)))

else:  # 2번 문제의 경우
    arr = list(map(int, m[1:]))
    cnt = 0
    
    # itertools를 사용하여 순열 생성 및 카운트
    for perm in itertools.permutations(range(1, n + 1)):
        cnt += 1
        if perm == tuple(arr):
            print(cnt)
            break
    