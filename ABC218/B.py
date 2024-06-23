P = list(map(int, input().split()))

#print(P)

for i in range(26):
  print(chr(P[i]+96), end="")