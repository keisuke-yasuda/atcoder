n, y = [int(i) for i in input().split()]
found = False
 
for i in range(n + 1):
  for j in range(n - i + 1):
    k = n - i - j
    if i * 10000 + j * 5000 + k * 1000 == y and not found:
      print('{} {} {}'.format(i, j, k))
      found = True
      break
        
if not found:
  print('-1 -1 -1')