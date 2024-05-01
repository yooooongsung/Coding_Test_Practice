n, k  = map(int,input().split())
t_arr = []
for _ in range(n):
    t = int(input())
    t_arr.append(t)

t_arr.sort(reverse=True)
cnt = 0
for i in t_arr:
    if i > k:
        continue
    cnt += k // i
    k %= i

print(cnt)