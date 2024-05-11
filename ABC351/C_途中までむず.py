N = int(input())
A =list(map(int,input().split()))

print(A)

cnt = 0
ans = 0
size = []
new_size = 0
for i in range(N):
  if i == 0:
    size.append(2**A[i])
  else:
    if 2**size[i-1] != 2**A[i]:
      size.append(2**A[i])
    else:
      new_size = size[i] + 2**A[i]
      size = size[:-1]
      size.append(new_size)
      for j <= range(1,len(size)):
        if size[-j] == size[-(j+1)]
        
  