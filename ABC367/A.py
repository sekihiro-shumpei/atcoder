A, B, C = map(int,input().split())

#print(A)

if B <= C:
  if B <= A <= C:
    print("No")
  else:
    print("Yes")
else:
  if C <= A <= B:
    print("Yes")
  else:
    print("No")