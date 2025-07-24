N, T, P = map(int, input().split())
L = list(map(int, input().split()))

#print(N, T, P)
#print(L)

#i = 0
ans = 0
num = 0
ans_num = []
while len(ans_num) < P:
  for i in range(len(L)):
    if L[i] >= T:
      #ans += 1
      ans_num.append(L[i])
      L[i] = 0
    elif L[i] != 0:
      L[i] += 1
  
  num += 1
  i = 0
  #print("ans_num:" + str(len(ans_num)))

#print(ans)
print(num-1)

        

  
  
    
  