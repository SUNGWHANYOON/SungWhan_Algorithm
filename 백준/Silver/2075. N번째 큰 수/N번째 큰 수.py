import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    for j in list(map(int,input().split())):
        arr.append(j)
    arr = sorted(arr,reverse=True)[0:n]

print(arr[n-1])
