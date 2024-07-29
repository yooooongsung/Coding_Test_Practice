s, p = map(int,input().split(' '))
dna = input()
part = list(map(int,input().split(' '))) #A, C, G, T
alphabet = ['A','C','G','T']
answer = ''

for i in range(4):
    x = alphabet[i]
    if part[i] > 0:
        if x in dna and len(answer) < p:
            for j in range(part[i]):
                answer += x
                dna = dna.replace(x,'')
                
print(answer)
        
            

            

