arr = {2 : ['A','B','C'],3 : ['D','E','F'],4 : ['G','H','I'],5 : ['J','K','L'],
        6 : ['M','N','O'],7 : ['P','Q','R','S'],8 : ['T','U','V'],
        9 : ['W','X','Y','Z'], 0 : ['OPERATOR']}

word = input()
answer = 0
for i in word:
    for k, v in arr.items(): 
        if i in v:
            answer += (k+1)

print(answer)
        
