import sys
from collections import deque
input = sys.stdin.readline

N,X = map(int,input().split())
visit = deque(list(map(int,input().split())))
arr = deque([])
for i in range(1,N,1):
    visit[i] += visit[i-1]

visit.appendleft(0)

answer = 0
count = 0

for i in range(X,N+1,1):
    arr.append(visit[i]-visit[i-X])

answer = max(arr)

if answer == 0:
    print('SAD')
else:
    print(answer)
    print(arr.count(answer))
