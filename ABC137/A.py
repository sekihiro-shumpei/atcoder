A, B = map(int, input().split())

ans = 0
ans = max(A+B, A-B, A*B)

print(ans)