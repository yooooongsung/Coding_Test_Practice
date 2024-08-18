import sys
input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int,input().split()))
stack = []

for i in arr:
    if i in stack:
        stack.append(i)
        answer = stack.count(i)
        if answer > k:
            stack.pop()
            print(len(stack))
            break
    else:
        stack.append(i)


# N, M = map(int, input().split())
# nums = list(map(int, input().split()))

# left, right = 0, 1
# cnt = 0
# while right<=N and left<=right:

#     sum_nums = nums[left:right]
#     total = sum(sum_nums)

#     if total == M:
#         cnt += 1

#         right += 1

#     elif total < M:
#         right += 1

#     else:
#         left += 1

# print(cnt)

