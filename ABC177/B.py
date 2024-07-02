S = str(input())
T = str(input())

cnt = 0
min_cnt = 100000
for i in range(len(S)-len(T)+1):
  cnt = 0
  for j in range(len(T)):
    if T[j] != S[i+j]:
      cnt += 1
      
  min_cnt = min(min_cnt, cnt)
      
print(min_cnt)

