#328.A
n:int
x:int
s = []
ans:int = 0

n, x = map(int,input().split())
s = list(map(int,input().split()))

for i in range(n):
  if s[i] <= x:
    ans += s[i]

print(ans)

