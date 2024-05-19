N = int(input())
S = []
C = []

for i in range(N):
  s,c = input().split()
  S.append(s)
  C.append(c)
  
#print(S)
#print(C)
C = list(map(int,C))
ans = sum(C) % N
S.sort()
print(S[ans])