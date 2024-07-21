import sys
input = sys.stdin.readline

n = int(input())
f = list(input().rstrip())
stack = []
arr = {}

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in range(n):
    arr[alphabet[i]]=int(input())


stack.append(f[0])
now = 1

while now < len(f):
    stack.append(f[now])

    if stack[-1]=='+':
        stack.pop()
        a = stack.pop()
        b = stack.pop()

        if a in alphabet:
            a = arr[a]
        if b in alphabet:
            b = arr[b]
        stack.append(b+a)

    if stack[-1]=='-':
        stack.pop()
        a = stack.pop()
        b = stack.pop()
        if a in alphabet:
            a = arr[a]
        if b in alphabet:
            b = arr[b]
        stack.append(b - a)

    if stack[-1]=='*':
        stack.pop()
        a = stack.pop()
        b = stack.pop()
        if a in alphabet:
            a = arr[a]
        if b in alphabet:
            b = arr[b]
        stack.append(b * a)

    if stack[-1]=='/':
        stack.pop()
        a = stack.pop()
        b = stack.pop()
        if a in alphabet:
            a = arr[a]
        if b in alphabet:
            b = arr[b]
        stack.append(b / a)

    now=now+1

    if now == len(f):
        print('%.2f'%(stack[-1]))
