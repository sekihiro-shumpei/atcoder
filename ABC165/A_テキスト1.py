K = int(input())
A, B = map(int, input().split())

ok = False

for x in range(A, B + 1):
  if x % K == 0:
    ok = True

if ok:
  print("OK")
else:
  print("NG")
