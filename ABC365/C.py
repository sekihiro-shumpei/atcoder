N , M = map(int, input().split())
A = list(map(int, input().split()))

#print(N, M, A)

if sum(A) <= M:
  print("infinite")
  exit()
  

avg = M // len(A)
#print(avg)

ans = 0

while True:
  for i in range(len(A)):
    ans += min(avg, A[i])
  
  if ans > M:
    print(avg-1)
    exit()
  else:
    avg += 1
    ans = 0