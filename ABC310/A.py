#ABC310.A

n:int
p:int
q:int
ans:int
s=[]

n, p, q = map(int,input().split())
s = list(map(int,input().split()))

ans = q + min(s)

if ans < p:
  print(ans)
else:
  print(p)


