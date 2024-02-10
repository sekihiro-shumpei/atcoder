#ABC320

s1:str
s2:str
start:int
end:int


s1 = input()
s2 = s1[::-1]
start = s1.find(s2)
print(start)
print(s2)
