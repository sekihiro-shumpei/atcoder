S = str(input())

while True:
  S = S[:-1]
  mid = len(S) //2
  
  if S[:mid] == S[mid:]:
    print(len(S[:mid]*2))
    exit()
    
    