K = int(input())
A, B = map(str, input().split())

A_10 = 0
A1 = int(A)
for i in range(len(A)):
  #while A1 // 10 > 0:
  A_10 += (A1 % 10) * (K**i)
  A1 //= 10
  #print(A1)

B_10 = 0
B1 = int(B)
for j in range(len(B)):
  #while A1 // 10 > 0:
  B_10 += (B1 % 10) * (K**j)
  B1 //= 10
  #print(A1)

#print(A_10)
#print(B_10)
print(A_10*B_10)   
