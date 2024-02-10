#326.B

n:int

ans:int = 0

n = int(input())

while (n // 100) * ((n // 10) % 10) != n % 10:
  n += 1

print(n)
