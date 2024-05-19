H = int(input())

high = 0
day = 0
for i in range(0,100000000):
  high += 2**i
  day += 1
  if high > H:
    print(day)
    exit()
  