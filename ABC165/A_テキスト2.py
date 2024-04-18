K = int(input())
A, B = map(int, input().split())

ok = False

for i in range(0, 10000000):
  if i * K > B:
    break
  
  if A <= i * K <= B:
    ok = True
    
if ok:
  print("OK")
else:
  print("NG")