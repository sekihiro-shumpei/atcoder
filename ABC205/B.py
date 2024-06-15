N = int(input())
A = list(map(int, input().split()))

A.sort()

#print(A)

for i in range(0,N-1):
  if A[i]+1 != A[i+1]:
    print("No")
    exit()
    
print("Yes")
  