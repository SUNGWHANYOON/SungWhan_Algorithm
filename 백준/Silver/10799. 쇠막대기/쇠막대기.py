import sys

input = sys.stdin.readline

arr = list(input().rstrip())
n = len(arr)

lazer = 0
stack = []

for i in range(1,n,1):
    if arr[i-1] =='(':
        lazer+=1
    if arr[i-1] == '(' and arr[i] ==')':
        lazer-=1

answer = lazer

for i in range(n):
    if arr[i] == '(':
        stack.append(i)
        continue

    index = stack.pop()
    if index + 1 == i:
        answer += len(stack)

print(answer)