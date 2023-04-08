s = int(input())
a = []

cnt = 0
a.append(s)

while True:
  if s % 2 == 0:
    s /= 2
    
  else:
    s = s * 3 + 1
  
  cnt += 1
  
  if s not in a:
      a.append(s)
    
  else:
      break
    
print(cnt+1)
  
  
  
  






