A, B = map(str, input().split())

a = int(A[0]) + int(A[1]) + int(A[2])
b = int(B[0]) + int(B[1]) + int(B[2])

if a >= b:
  print(a)
else:
  print(b)

