import sys

n:int
h:int
x:int
p = []
ans:int

n, h, x = map(int,input().split())
p = list(map(int,input().split()))

for i in range(n):
    if h + p[i] >= x:
        print(i + 1)
        sys.exit()
