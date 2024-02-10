#329.B できてない

n:int
a = []

n = int(input())
a = list(map(int,input().split()))

#print(a)

a = list(set(a))

print(a[-2])
