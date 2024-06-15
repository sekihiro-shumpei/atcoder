N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))

old_kion = 100000000
now_kion = 0

for i in range(N):
  now_kion = T - H[i] * 0.006
  if abs(now_kion-A) < abs(old_kion-A):
    old_kion = now_kion
    ans = i+1
    
print(ans)