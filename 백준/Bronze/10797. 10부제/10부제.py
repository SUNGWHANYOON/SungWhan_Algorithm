n = int(input())
arr = list(map(int,input().split()))
answer = 0
for i in arr:
    if i%10 == n:
        answer+=1

print(answer)