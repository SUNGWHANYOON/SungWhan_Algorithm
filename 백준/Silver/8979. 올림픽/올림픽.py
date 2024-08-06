import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

arr = []
find_nation_data = 0

for i in range(n):
    score = deque(list(map(int,input().split())))
    nation = score.popleft()

    if nation == k:
        find_nation_data = list(score)
    arr.append(list(score))

arr = sorted(arr,reverse=True)
answer = 1
for rank in arr:
    if rank == find_nation_data:
        break
    answer+=1

print(answer)