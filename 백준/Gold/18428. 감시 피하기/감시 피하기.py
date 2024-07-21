import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = []

blank = []
T = []

for i in range(n):
    arr.append(list(map(str,input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X':
            blank.append([i,j])

        if arr[i][j] =='T':
            T.append([i,j])

cand = list(combinations(blank,3))

for a,b,c in cand:

    part = 1
    x1,y1=a
    x2,y2=b
    x3,y3=c

    arr[x1][y1] = 'O'
    arr[x2][y2] = 'O'
    arr[x3][y3] = 'O'

    for Tx,Ty in T:
        for i in range(Tx,n,1):
            if arr[i][Ty] == 'O':
                break

            if arr[i][Ty] == 'S':
                part = 0
                break

        for i in range(Tx,-1,-1):
            if arr[i][Ty] == 'O':
                break

            if arr[i][Ty] == 'S':
                part = 0
                break

        for i in range(Ty,n,1):
            if arr[Tx][i] == 'O':
                break

            if arr[Tx][i] == 'S':
                part = 0
                break

        for i in range(Ty,-1,-1):
            if arr[Tx][i] == 'O':
                break

            if arr[Tx][i] == 'S':
                part = 0
                break

    if part:
        print('YES')
        exit(0)

    arr[x1][y1] = 'X'
    arr[x2][y2] = 'X'
    arr[x3][y3] = 'X'

print('NO')