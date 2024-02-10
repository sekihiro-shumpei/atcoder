#ABC322.A

n:int
s:str
cnt:int = 0

n = int(input())
s = str(input())

for i in range(n-2):
  if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
    cnt = i + 1
    break

if cnt == 0:
  cnt = -1

print(cnt)


