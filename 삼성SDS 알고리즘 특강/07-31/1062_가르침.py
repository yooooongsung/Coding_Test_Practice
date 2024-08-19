import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1 ##bit masking##


def dfs(idx, cnt):
    global answer

    if cnt == k - 5: #a,c,i,n,t를 제외한 나머지 가르칠 수 있는 알파벳의 수 == cnt
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]: #만약 입력받은 단어가 배울 수 없는, 즉 learn의 값이 0인 경우
                    check = False #flag를 False로 만들고
                    break #for문 종료
            if check: 
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26): #cnt는 초기값이 0 >> k-5개와 나머지 가르칠 수 있는 알파벳의 수가 다르다면 for문
        if not learn[i]: #a,c,i,n,t를 제외한 나머지 알파벳들 찾기
            learn[i] = True #해당 알파벳을 1로 만들고
            dfs(i, cnt + 1) #dfs함수를 돈다 >> 어차피 b가 추가될 것이고 이는 31번째 줄에서 디버깅 가능함
            learn[i] = False #


dfs(0, 0)
print(answer)
