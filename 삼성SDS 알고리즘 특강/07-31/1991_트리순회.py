import sys
n = int(input())
dic = {}
for _ in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    dic[root] = [left,right]

def pre(root): #딕셔너리의 시작 값의 1번째 요소 == 딕셔너리의 다른 키값 >>> 반복
    if root != '.':
        print(root, end='')
        pre(dic[root][0])
        pre(dic[root][1])



def inorder(root):
    if root != '.':
        inorder(dic[root][0])
        print(root, end='')
        inorder(dic[root][1])

def post(root):
    if root != '.':
        post(dic[root][0])
        post(dic[root][1])
        print(root, end='')

pre('A')
print()
inorder('A')
print()
post('A')

