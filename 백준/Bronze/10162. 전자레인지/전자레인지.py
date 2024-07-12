n = int(input())
if n%10:
    print(-1)
else:
    print(n//300,end=' ')
    n = n%300
    print(n//60,end= ' ')
    n = n%60
    print(n//10)