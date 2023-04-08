s = int(input())
a = []

cnt = 0
x = s
y = 0
a.append(s)

while x != y:
    if s % 2 == 0:
        s /= 2
        cnt += 1
        if s not in a:
            a.append(s)
            y = s
        else:
            break

    else:
        s = s * 3 + 1
        cnt += 1
        if s not in a:
            a.append(s)
            y = s
        else:
            break

print(cnt+1)
