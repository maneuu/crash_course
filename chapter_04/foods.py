# Copiando uma lista

my_foods =  ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli') 
friend_foods.append('ice cream')
print("My favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:") 
print(friend_foods)

print("\n","# # " * 10,end="\n\n")

my_foods =  ['pizza', 'falafel', 'carrot cake']
# o que vem a seguir não funciona para copiar uma lista
friend_foods = my_foods
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:") 
print(my_foods)
print("\nMy friend's favorite foods are:") 
print(friend_foods)

