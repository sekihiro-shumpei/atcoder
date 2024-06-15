def is_post(S, A, B):
  if S[A] != "-":
    return False
    
  if len(S) != A+B+1:
    return False
    
  for i in range(len(S)):
    if i != A and not S[i].isdigit():
      return False
      
  return True


A, B = map(int, input().split())
S = input()

if is_post(S,A,B):
  print("Yes")
else:
  print("No")

