N, M = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(N):
  if cnt <= M:
    if cnt + H[i] <= M:
      ans += 1
    cnt += H[i]
    
    
print(ans)