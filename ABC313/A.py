#ABC313.A

n:int
p = []
p_max:int
p_max_2:int
ans:int

n = int(input())
p = list(map(int, input().split()))

p_max = max(p)
ans = (p_max + 1) - p[0]

if ans == 1:
ans = 0

p.remove(max(p))
p_max_2 = max(p)
if p_max == p_max_2:
ans = 1

print(ans)

