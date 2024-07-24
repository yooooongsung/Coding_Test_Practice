S, P = map(int, input().split())
dna = list(input())
tmp = list(map(int, input().split()))
given_num = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
part_num = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

cnt = 0
for i in range(S-P+1):
    flag = True

    if i == 0:
        for j in range(P):
            part_num[dna[j]] += 1
    else:
        part_num[dna[i+P-1]] += 1
        part_num[dna[i-1]] -= 1

    for i in ('A', 'C', 'G', 'T'):
        if part_num[i] < given_num[i]:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)