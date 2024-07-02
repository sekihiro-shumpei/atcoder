A = []
for i in range(3):
  a = list(map(int,input().split()))
  A.append(a)
  
N = int(input())

zero = []
for i in range(3):
  z = []
  for j in range(3):
    z.append(0)
  zero.append(z)
#print(A)
#print(zero)

for B in range(N):
  b = int(input())
  for i in range(3):
    for j in range(3):
      if b == A[i][j]:
        zero[i][j] = 1
        
#print(zero)
judge = False
for i in range(3):
  if zero[i][0] + zero[i][1] + zero[i][2] == 3:
    judge = True
  if zero[0][i] + zero[1][i] + zero[2][i] == 3:
    judge = True
    
if zero[0][0] + zero[1][1] + zero[2][2] == 3:
  judge = True
if zero[0][2] + zero[1][1] + zero[2][0] == 3:
  judge = True
  
if judge:
  print("Yes")
else:
  print("No")