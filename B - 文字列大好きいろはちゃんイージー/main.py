n, l = [int(i) for i in input().split()]
 
strings = []
 
for i in range(n):
  strings.append(input())
 
strings.sort()
 
print(''.join(strings))