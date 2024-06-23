n, a = map(int, input().split())
t = list(map(int, input().split()))
pre = 0

for i in range(n):
  ans = max(pre, t[i])+a
  print(ans)
  pre = ans