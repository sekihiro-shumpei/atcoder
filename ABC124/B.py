N = int(input())
H = list(map(int, input().split()))

ans = 1
now = H[0]
for i in range(1, N):
  #print(i)
  if H[i] >= now:
    ans += 1
    now = H[i]
    
print(ans)
  