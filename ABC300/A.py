N, A, B = map(int, input().split())
C = list(map(int, input().split()))

for i in range(N):
  if C[i] == A+B:
    print(i+1)
