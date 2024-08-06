import sys
s = list(input())
t = list(input())

def change(t):
    if s == t:
        print(1)
        sys.exit()
    if len(t) == 0:
        return
    if t[-1] == 'A':
        change(t[:-1])
    if t[0] == 'B':
        change(t[1:][::-1])
change(t)
print(0)
