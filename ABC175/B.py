N = int(input())
L = list(map(int, input().split()))

ans = 0
cnt = 0


for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if L[i] < L[j]+L[k] and L[j] < L[i]+L[k] and L[k] < L[j]+L[i]:
        if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:
          ans += 1
      cnt += 1
        
print(ans)
#print(cnt)
      