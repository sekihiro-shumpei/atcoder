#ABC321.A

n:int

n = int(input())
like_number = []
sort_number = []

while n > 0:
  like_number.append(n%10)
  n //= 10

like_number.reverse()
sort_number = sorted(like_number,reverse = True)


if like_number == sort_number and len(set(like_number)) == len(like_number):
  print("Yes")
else:
  print("No")

#print(like_number)
#print(sort_number)
