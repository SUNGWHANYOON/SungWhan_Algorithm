import sys

input = sys.stdin.readline

input()

arr = list(input().rstrip())
if arr.count('A') > arr.count('B'):
    print('A')
elif arr.count('A') == arr.count('B'):
    print('Tie')
else:
    print('B')