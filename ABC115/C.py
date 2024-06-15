N, K = map(int, input().split())

H = []
for i in range(N):
  h = int(input())
  H.append(h)
  
#print(H)

H.sort()
#print(H)
old_ans = 1000000000000
for i in range(0,N-K+1):
  new_ans = H[(i+K)-1] - H[i]
  ans = min(new_ans, old_ans)
  if new_ans < old_ans:
    old_ans = new_ans
  
  
print(ans)