import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

F = {}
NGF = [-1]*n

stack = []

for i in range(n):
    if arr[i] not in F:
        F[arr[i]] = 1
    else:
        F[arr[i]]+=1

for i in range(n):
    while stack and F[arr[i]] > F[arr[stack[-1]]]:
        NGF[stack.pop()] = arr[i]
    stack.append(i)

print(*NGF)