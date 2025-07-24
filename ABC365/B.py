N =int(input())
A = list(map(int, input().split()))
A_sort = sorted(A, reverse=True)
#print(N, A, A_sort)

second = A_sort[1]
#print(second)

for i in range(len(A)):
  if second == A[i]:
    print(i+1)
    exit()

