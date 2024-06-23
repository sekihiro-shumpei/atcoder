S = str(input())

S_reverse = S[::-1]

ans = 0

for i in range(len(S)):
  if S[i] != S_reverse[i]:
    ans += 1
    
print(ans//2)