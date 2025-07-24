#X = list(map(float, input().split()))
X = list(input())

# print(X)

for i in range(len(X)):
    if X[-i] != "0" or X[-i] == ".":
        X = map(str, X)
        X = ''.join(X)
        print(X)
        exit()
    else:
        X.pop
        i -= 1



#なんかXが文字列型だと、popが適用されんっぽいね