from re import X


x_1, y_1 = map(int,input().split())
x_2, y_2 = map(int,input().split())
x_3, y_3 = map(int,input().split())

x_4 = int
y_4 = int

x_4 = x_1 ^ x_2 ^ x_3
y_4 = y_1 ^ y_2 ^ y_3

print(x_4, y_4)
