n,m = map(int,input().split())

arr = [[x]*x for x in range(1001)]
arr2 = []

for x in arr:
    for y in x:
        arr2.append(y)

print(sum(arr2[n-1:m]))
