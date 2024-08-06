import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

arr = []

for i in range(n):
    score = deque(list(map(int,input().split())))
    nation = score.popleft()
    score.append(nation)
    arr.append(list(score))

arr = sorted(arr,reverse=True)

answer = 1

for i in range(1,n):
    if arr[i][0:3] != arr[i-1][0:3]:
        answer+=1

    if arr[i][3] == k:
        print(answer)
        exit(0)