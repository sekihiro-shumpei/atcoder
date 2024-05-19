N = int(input())
user_array = []
for _ in range(N):
  s, c = input().split()
  user_array.append((s, int(c)))

user_array.sort()
T = 0
for user in user_array:
  _name, rating = user
  T += rating
  
winner_index = T % N
winner = user_array[winner_index]
print(winner[0])