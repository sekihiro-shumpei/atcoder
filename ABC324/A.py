#ABC324.A

n:int
a = []
ans:str

n = int(input())
a = list(map(int,input().split()))
#print(a)

for i in range(n):
  if a[i] != a[0]:
    ans = "No"
    break
  else:
    ans = "Yes"

print(ans)


