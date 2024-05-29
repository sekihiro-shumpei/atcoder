N, K = map(int, input().split())

for i in range(K):
  if N % 200 == 0:
    N = N // 200
  else:
    N = str(N)
    N = N + str(200)
    #print(N)
    N = int(N)
    
print(N)