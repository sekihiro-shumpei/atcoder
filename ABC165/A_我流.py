import sys

k:int
a:int
b:int
i:int=1

k = int(input())
a, b = map(int,input().split())

#print(k,a,b)

while k * i <= b:
  if a <= k*i <= b:
    print("OK")
    sys.exit()
    
  #print(i)
  i += 1
  
print("NG")
  
