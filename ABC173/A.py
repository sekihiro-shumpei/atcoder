N = int(input())

if N % 1000 > 0:
  print(1000*(N // 1000 + 1) - N)
else:
  print(0)