R = int(input())
ans = 0

if R <= 99:
  ans = 100 - R
elif R <= 199:
  ans = 200 - R
elif R <= 299:
  ans = 300 - R

print(ans)