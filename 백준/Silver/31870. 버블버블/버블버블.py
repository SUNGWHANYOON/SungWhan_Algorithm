import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ar = arr[:]
answer1 = 0
for i in range(n):
    for j in range(i,n,1):
        if i != j and arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            answer1+=1

answer2 = 0
for i in range(n):
    for j in range(i,n,1):
        if i != j and ar[i] < ar[j]:
            temp = ar[i]
            ar[i] = ar[j]
            ar[j] = temp
            answer2+=1
print(min(answer1,answer2+1))