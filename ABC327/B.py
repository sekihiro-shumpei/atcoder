#ABC327.B
import math


b:int

b = int(input())


sqrt_b = math.isqrt(b)
print()
if sqrt_b ** sqrt_b == b:
  print(sqrt_b)
else:
  print(-1)

print(sqrt_b)



