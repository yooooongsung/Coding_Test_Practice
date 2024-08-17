import sys
input = sys.stdin.readline
n = int(input())
main = list(input())
answer = 0

for _ in range(n-1):
    x = input()
    compare = main.copy() #main이라는 단어를 카피해서 비교할 것임
    cnt = 0
    for i in x:
        if i in compare:
            compare.remove(i)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)