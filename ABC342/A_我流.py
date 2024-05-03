from collections import Counter

S:str
cnt:int = 0

S = input()

counts = Counter(S)
unique_char = next(char for char, count in counts.items() if count == 1)

print(S.index(unique_char) + 1)
  