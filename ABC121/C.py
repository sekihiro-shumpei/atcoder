N, M = map(int, input().split())

ans = 0
cnt = 0
shop = []

for i in range(N):
  A,B = map(int,input().split())
  shop.append((A,B))

shop.sort(key=lambda x: x[0])
  
#print(shop)

for i in range(N):
  if cnt >= M:
      break
  for j in range(shop[i][1]):
    cnt += 1
    ans += shop[i][0]
    #print(ans)
    #print(cnt)
  
    if cnt >= M:
      break
  
  
print(ans)