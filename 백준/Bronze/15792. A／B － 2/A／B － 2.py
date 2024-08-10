a,b = map(int,input().split())

count = 0

print(a//b,end='')
print('.',end='')
a = a%b
while count <= 1001:
    count+=1

    res = (a*10)%b
    div = (a*10)//b

    print(div,end='')
    a = res
