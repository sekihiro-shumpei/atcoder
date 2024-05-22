N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
  if A[i] > 10:
    ans += abs(10 - A[i])

print(ans)