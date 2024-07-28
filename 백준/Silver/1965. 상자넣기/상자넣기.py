import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

dp = [0]*n

for i in range(n):
    for j in range(i+1,n,1):
        if arr[j] > arr[i]:
            if dp[i]+1 > dp[j]:
                dp[j] = dp[i]+1

print(max(dp)+1)