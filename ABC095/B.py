N, X = map(int, input().split())

donuts = []
cnt = 0
for i in range(N):
  m = int(input())
  donuts.append(m)
  
#print(donuts)
X = X - sum(donuts)
cnt = N + X // min(donuts)

print(cnt)
