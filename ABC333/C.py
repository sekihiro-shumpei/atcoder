#ABC333.C not complete
import sys

n:int
ans:int = 3
cnt:int = 1
repyu:int = 10

n = int(input())

if n == 1:
  print(ans)
  sys.exit()


while cnt < n:
  for i in range(3):
    ans +=  repyu
    cnt += 1
    print(ans)
    print(cnt)
    if cnt == n:
      break

  repyu = repyu * 10
  #cnt +=1

print(ans)
