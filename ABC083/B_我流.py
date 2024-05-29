N, A, B = map(int, input().split())

ans = 0
number = 0
total = 0
for i in range(1, N+1):
  number = i
  while number > 0:
    total += number % 10
    number //= 10
    
  if A <= total <= B:
    ans += i
    
  total = 0
    
  
print(ans)
    