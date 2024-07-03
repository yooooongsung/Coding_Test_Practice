n = int(input())
d = [input() for _ in range(n)]
y = [input() for _ in range(n)]

answer = 0
for i in range(n):
    x = d[i]
    if d.index(x) > y.index(x):
        answer += 1

print(answer)