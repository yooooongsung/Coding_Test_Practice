arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

string = input()
answer = 0

for i in range(len(arr)):
    if arr[i] in string:
        answer += string.count(arr[i])
        string = string.replace(arr[i],' ')

for i in string:
    if i != ' ':
        answer += 1

print(answer)