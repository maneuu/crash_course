my_foods =  ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli') 
friend_foods.append('ice cream')

for food in my_foods:
  print(f"I like {food}")

print("\n")

for food in friend_foods:
  print(f"My friends like {food}")