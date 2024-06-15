N, M = map(int,input().split())
A = list(map(int,input().split()))

X = []
for i in range(N):
  x = list(map(int,input().split()))
  X.append(x)
  
#print(X)

for j in range(M):
  s = 0
  for i in range(N):
    s += X[i][j]
  if s < A[j]:
    print("No")
    exit()
      
print("Yes")
  