S = str(input())
T = str(input())

S_judge = S
if S_judge == T:
    print("Yes")
    exit()
    
for i in range(len(S)-1):
  
  S_judge= S[:i] + S[i+1] + S[i] + S[i+2:]
  #S = S[-1] + S[:-1]
  #print(S_judge)
  
  if S_judge == T:
    print("Yes")
    exit()
  
print("No")