N = int(input())

mnt = []
for i in range(N):
  m = input().split()
  name = m[0]
  height = int(m[1])
  mnt.append((name, height))
  
#print(mnt)

mnt.sort(key=lambda x: x[1], reverse=True)

#print(mnt)

print(mnt[1][0])
  