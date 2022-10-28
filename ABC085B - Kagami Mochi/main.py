n = int(input())
d = set()
count = 1
 
def get_big_and_small(d):
  big = max(d)
  d.remove(big)
  small = max(d)
  return big, small
 
for i in range(n):
  d.add(int(input()))
 
while len(d) > 1:
  big, small = get_big_and_small(d)
  if big > small:
    count += 1
  else:
    break
  
print(count)