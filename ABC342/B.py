N:int = 0
P = []
Q:int = 0

N = input()
P = list(map(int, input().split()))
Q = int(input())


for i in range(Q):
  A, B = map(int, input().split())
  #print(P.index(A))
  #print(P.index(B))
  if P.index(A) < P.index(B):
    print(P[P.index(A)])
  else:
    print(P[P.index(B)])


