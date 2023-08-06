#ABC311.A

n:int
s:str
cnt_a:int=0
cnt_b:int=0
cnt_c:int=0

n = int(input())
s = str(input())

for i in range(n):
  if s[i] == "A":
    cnt_a += 1
  elif s[i] == "B":
    cnt_b += 1
  else:
    cnt_c += 1

  if cnt_a != 0 and cnt_b != 0 and cnt_c != 0:
    break

print(i+1)


