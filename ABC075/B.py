DX = [1,0,-1,0,1,-1,-1,1]
DY = [0,1,0,-1,1,1,-1,-1]

H, W = map(int, input().split())

S = []
for i in range(H):
  s = input()
  S.append(s)
 
result = []
for row in S:
  new_row = []
  for v in row:
    if v == ".":
      new_row.append(0)
    else:
      new_row.append("#")
      
  result.append(new_row)

#print(S)
#print(result)

for i in range(H):
  for j in range(W):
    if S[i][j] != ".":
      continue
    
    for dx, dy in zip(DX, DY):
      ni, nj = i + dx, j + dy
      
      if ni < 0 or ni >= H or nj < 0 or nj >= W:
        continue
      
      if S[ni][nj] == "#":
        result[i][j] += 1
        
for row in result:
  print(*row, sep='')
    

 
 
  
#print(S)

#S = [input() for i in range(H)]
#result = [[0 if v=='.' else '#' for v in row]for row in S]
#print(result)