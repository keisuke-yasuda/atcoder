n,a,b = [int(i) for i in input().split()]
ans = 0
 
def check_num(i):
  i += 1
  if i >= 10:
    k = [int(j) for j in str(i)]
    if sum(k) <= b and sum(k) >= a:
      return i
    else:
      return 0
  elif i <= b and i >= a:
    return i
  else:
    return 0
 
for i in range(n):
  ans += check_num(i)
  
print(ans)