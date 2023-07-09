import sys

n: int
i: int
array = []

array = list(map(int, input().split()))
n = len(array)

for i in range(0,n):
  if i < 7 and array[i] > array[i+1]:
    print('No')
    sys.exit()
  elif array[i] < 100 or array[i] > 675:
    print('No')
    sys.exit()
  elif array[i] % 25 != 0:
    print('No')
    sys.exit()

print('Yes')


