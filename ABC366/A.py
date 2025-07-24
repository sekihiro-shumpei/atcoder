N, T, A = map(int, input().split())

judge_N = (N // 2) + 1
#print(judge_N)

if A >= judge_N or T >= judge_N:
  print("Yes")
else:
  print("No")