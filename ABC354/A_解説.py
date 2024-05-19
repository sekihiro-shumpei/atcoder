H = int(input())

high=0
cnt=0

while high <= H:
  high += 2**cnt
  cnt+= 1
  
print(cnt)

解説ではwhile文を使って実装