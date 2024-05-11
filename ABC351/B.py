N = int(input())

A = []
B = []
for i in range(N):
  a = input()
  A.append(a)
  
for i in range(N):
  b = input()
  B.append(b)
  
for i in range(N):
  for j in range(N):
    if A[i][j] != B[i][j]:
      print(i+1, j+1)

