N = int(input())
A = list(map(int, input().split()))

cnt = 0
ans = 0
i = 0
#while N > 0:
while i != N:
  if A[i] % 2 != 0:
    break
  
  if A[i] % 2 == 0:
    cnt += 1
    A[i] //= 2
    
  if N == cnt:
    ans += 1
    cnt = 0
    i = -1
    
  i += 1
  
  #print(A)  
      
    
    
  #break

print(ans)