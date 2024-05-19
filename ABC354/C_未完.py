N = int(input())
A = []
C = []

for i in range(N):
  a,c = map(int, input().split())
  A.append(a)
  C.append(c)

cnt = 0
ans = []
for i in range(N):
  for j in range(i,N):
    if A[i] < A[j] and C[i] > C[j]:
      ans.append(A[i])
      
num_A = A    
set_A = set(num_A)
set_ans = set(ans)
common_elements = set_A & set_ans
num_A = [x for x in A if x not in common_elements]      

indexes = [i for i, x in enumerate(A) if x  in num_A]


print(len(num_A)) 
for index in indexes:
    print(index+1, end=" ")
#print(len(num_A))
#print(A)  