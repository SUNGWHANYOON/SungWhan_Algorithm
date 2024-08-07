n = int(input())

left = 0
right = 0
nsum = 0
answer = 0
while left <= right <= n+1:
    if nsum == n:
        answer+=1

    if nsum > n:
        nsum-=left
        left+=1
        continue

    if nsum <= n:
        nsum += right
        right+=1

print(answer)