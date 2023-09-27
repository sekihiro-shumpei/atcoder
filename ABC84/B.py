a:int
b:int
s:str
post_number:str

a, b = map(int,input().split())
s = input()
#print(len(s))
if len(s) == a + b + 1 and s[a] == "-":
    #print(s)
    s = s.replace("-","")
    #print(s.isdecimal())
    #print(s)
    if s.isdecimal():
        print("Yes")
    else:
        print("No")
else:
    print("No")

