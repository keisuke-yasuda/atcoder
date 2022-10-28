s = input()
 
ans = ''
 
for i in s:
  if i == '0':
    ans = ans + i
  elif i == '1':
    ans = ans + i
  elif i == 'B':
    ans = ans[:-1]
    
print(ans)