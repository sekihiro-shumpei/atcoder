#ABC307.A
n: int = 0
i: int
j: int
cnt:int = 0
s = []
ans: int = 0


n = int(input())
s = list(map(int,input().split()))

for i in range(0,n):
  for j in range(7):
    ans += s[cnt]
    cnt += 1
  print (ans)
  ans = 0





