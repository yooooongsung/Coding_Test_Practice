import sys
cnt = 0
dic = {}
answer = []
while True:
    x = sys.stdin.readline().strip()
    if not x:
        break
    cnt +=1 
    if x not in dic.keys():
        dic[x] = 1
    else:
        dic[x] += 1

for k, v in dic.items():
    percent = v / cnt * 100
    answer.append(k + ' ' + str(percent))

answer.sort()
for i in answer:
    print(i)
