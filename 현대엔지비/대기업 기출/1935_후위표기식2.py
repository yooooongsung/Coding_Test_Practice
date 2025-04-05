import sys
import string
input = sys.stdin.readline
n = int(input())
notation = input().strip()
converted = []

value = [int(input()) for i in range(n)]
alphabet = list(string.ascii_uppercase[:n])
dic = dict(zip(alphabet, value))

for char in notation:
    if char in dic: #key가 dic에 있다면
        converted.append(dic[char]) # 알파벳이면 대응 숫자로
    elif char == '*':
        a = float(converted.pop())
        b = float(converted.pop())
        cal = a * b
        converted.append(cal)

    elif char == '+':
        a = float(converted.pop())
        b = float(converted.pop())
        cal = a + b
        converted.append(cal)

    elif char == '-':
        a = float(converted.pop())
        b = float(converted.pop())
        cal = b - a
        converted.append(cal)

    elif char == '/':
        a = float(converted.pop())
        b = float(converted.pop())
        cal = b / a
        converted.append(cal)


print(f"{converted[0]:.2f}") #자릿수 출력 포맷

