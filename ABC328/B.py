#328.B

n:int
d = []
ans:int = 0

n = int(input())
d = list(map(int,input().split()))

for i in range(n):
  month_str = str(i+1)
  for j in range(d[i]):
    day_str = str(j+1)
    if len(set(month_str + day_str)) == 1:
      ans += 1

print(ans)


