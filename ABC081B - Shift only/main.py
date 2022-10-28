n = input()
num_list = map(int, input().split())
num_list = [int(i) for i in num_list]
  
def check_even_num():
  count = 0
  while True:
    for i in range(len(num_list)):
      if num_list[i] % 2 == 0:
        num_list[i] /= 2
      else:
        return count
    count += 1
    
count = check_even_num()
      
print(count)