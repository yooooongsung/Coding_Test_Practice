import sys
import string
input = sys.stdin.readline
n = int(input())
notation = input().strip()

value = [int(input()) for i in range(n)]
alphabet = list(string.ascii_uppercase[:n])
dic = dict(zip(alphabet, value))




# while i < len(notation):
#     if notation[i] == '*':
#         notation[i-2] = dic[notation[i-2]] * dic[notation[i-1]]
#         notation[i-1] = ''
#         notation[i] = ''
#         i = 0
#     elif notation[i] == '/':
#         notation[i-2] = str(dic[notation[i-2]] / dic[notation[i-1]])
#         notation[i-1] = ''
#         notation[i] = ''
#         i = 0
#     elif notation[i] == '+':
#         notation[i-2] = str(dic[notation[i-2]] + dic[notation[i-1]])
#         notation[i-1] = ''
#         notation[i] = ''
#         i = 0
#     elif notation[i] == '-':
#         notation[i-2] = str(dic[notation[i-2]] - dic[notation[i-1]])
#         notation[i-1] = ''
#         notation[i] = ''
#         i = 0
#     i += 1

# print(notation)