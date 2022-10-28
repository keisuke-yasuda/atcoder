n = int(input())
cards = [int(i) for i in input().split()]
 
a_score = 0
b_score = 0
 
for i in range(len(cards)):
  if i % 2 == 0:
    a_score += max(cards)
  else:
    b_score += max(cards)
  cards.remove(max(cards))
    
print(a_score - b_score)