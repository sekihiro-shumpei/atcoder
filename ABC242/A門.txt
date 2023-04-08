A, B, C, X = map(int,input().split())
kakuritu = float
member = int


if X <= A:
  kakuritu = 1
  
elif A < X <= B:
  kakuritu = C / (B-A)
  
else:
  kakuritu = 0
    
print(kakuritu)
  