k, n = map(int,input().split(' '))
given = []

for _ in range(k):
    x = int(input())
    given.append(x)


def bn_search(start, end, count, n):
    answer = []
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(k):
            x = given[i] // mid
            count += x

        if count >= n:
            start = mid + 1
            answer.append(mid)
        elif count < n:
            end = mid - 1
    return max(answer)
start = 1
end = max(given) 
count = 0

print(bn_search(start, end, count, n))