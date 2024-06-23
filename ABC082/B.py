s = str(input())
t = str(input())

s_list = list(s)
t_list = list(t)

s_list.sort()
t_list.sort(reverse=True)

s_judge = ''.join(s_list)
t_judge = ''.join(t_list)

if s_judge < t_judge:
  print("Yes")
else:
  print("No")