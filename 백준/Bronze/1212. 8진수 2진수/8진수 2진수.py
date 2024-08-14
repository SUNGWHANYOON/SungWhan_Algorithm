import sys
n = list(input().rstrip())

arr = []

div8 = ['000','001','010','011','100','101','110','111']
for i in n:
    r = int(i)
    arr.append(div8[r])

start = 0

if arr==['000']:
    print(0)
    exit(0)

cond = 0
for c in "".join(arr):
    if c == '1':
        cond+=1

    if cond>=1:
        print(c,end='')

